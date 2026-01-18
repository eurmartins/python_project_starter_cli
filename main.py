import os
import shutil
import click
import questionary

DIRETORY_TEMPLATES = os.path.join(os.path.dirname(__file__), "templates")


def copy_template(
    framework,
    project_name,
    libs=None,
    db=None,
    db_user=None,
    db_password=None,
    db_host=None,
    db_port=None,
):
    src = os.path.join(DIRETORY_TEMPLATES, framework)
    dst = os.path.join(os.getcwd(), project_name)
    shutil.copytree(src, dst)
    req_path = os.path.join(dst, "requirements.txt")
    db_lib = None
    db_settings = ""
    if db:
        if db == "postgres":
            if framework in ["django", "flask"]:
                db_lib = "psycopg2-binary"
            else:
                db_lib = "asyncpg"
        elif db == "mysql":
            if framework in ["django", "flask"]:
                db_lib = "mysqlclient"
            else:
                db_lib = "aiomysql"
        elif db == "sqlite":
            db_lib = None
    if db_lib:
        with open(req_path, "a", encoding="utf-8") as f:
            f.write(f"\n{db_lib}")
    if libs:
        if os.path.exists(req_path):
            with open(req_path, "a", encoding="utf-8") as f:
                for lib in libs:
                    f.write(f"\n{lib}")
        else:
            with open(req_path, "w", encoding="utf-8") as f:
                for lib in libs:
                    f.write(f"{lib}\n")
    if db and db != "sqlite":
        env_path = os.path.join(dst, ".env.example")
        if os.path.exists(env_path):
            with open(env_path, "a", encoding="utf-8") as f:
                if db == "postgres":
                    f.write(
                        f"\nDATABASE_URL=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/mydb"
                    )
                elif db == "mysql":
                    f.write(
                        f"\nDATABASE_URL=mysql://{db_user}:{db_password}@{db_host}:{db_port}/mydb"
                    )


@click.command()
@click.option(
    "--framework",
    type=click.Choice(["fastapi", "flask", "django"]),
    prompt=True,
    help="Escolha o framework",
)
@click.option("--name", prompt="Nome do projeto", help="Nome do projeto")
@click.option(
    "--libs",
    multiple=True,
    help="Bibliotecas adicionais para adicionar ao requirements.txt (pode usar múltiplas vezes)",
)
@click.option(
    "--db",
    type=click.Choice(["sqlite", "postgres", "mysql"]),
    prompt=True,
    help="Banco de dados para o projeto",
)
def main(framework, name, libs, db):
    popular_libs = [
        "requests",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "pytest",
        "black",
        "isort",
        "mypy",
        "pydantic",
        "celery",
        "redis",
        "docker",
        "kubernetes",
        "awscli",
        "boto3",
    ]

    add_libs = click.confirm(
        "Deseja adicionar bibliotecas populares ao projeto?", default=False
    )
    selected_libs = list(libs)
    if add_libs:
        selected = questionary.checkbox(
            "Selecione as bibliotecas que deseja adicionar:", choices=popular_libs
        ).ask()
        if selected:
            selected_libs.extend(selected)

    db_user = None
    db_password = None
    db_host = None
    db_port = None
    if db != "sqlite":
        db_user = click.prompt("Usuário do banco", default="root")
        db_password = click.prompt("Senha do banco", default="", hide_input=True)
        db_host = click.prompt("Host do banco", default="localhost")
        db_port = click.prompt(
            "Porta do banco", default="5432" if db == "postgres" else "3306"
        )
    copy_template(
        framework, name, selected_libs, db, db_user, db_password, db_host, db_port
    )
    click.secho(f"Projeto {name} criado com base no template {framework}!", fg="green")
    if selected_libs:
        click.secho(f"Bibliotecas adicionadas: {', '.join(selected_libs)}", fg="yellow")
    click.secho(f"Banco de dados configurado: {db}", fg="cyan")


if __name__ == "__main__":
    main()
