from django.http import JsonResponse
from ..usecases.hello_usecase import HelloUseCase

def hello_view(request):
    name = request.GET.get('name', 'World')
    usecase = HelloUseCase()
    message = usecase.execute(name)
    return JsonResponse({'message': message})