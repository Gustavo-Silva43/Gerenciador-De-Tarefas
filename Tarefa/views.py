# app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Item # Certifique-se de que seus campos em models.py estão em snake_case!

# Create your views here.
def criar_item(request):
    return render(request, 'app/criar.html')

def cadastro(request):
    if request.method == "POST":
        print("Dados recebidos no POST:", request.POST) # Mantenha para depuração

        # --- AQUI ESTAVA O PONTO CRÍTICO! ---
        # 1. As chaves de request.POST.get() DEVEM ser IGUAIS aos 'name' dos inputs no HTML (tudo snake_case).
        # 2. As variáveis locais (nome, cpf, etc.) DEVEM ser snake_case para clareza.
        # 3. Os argumentos do construtor Item(...) DEVEM ser IGUAIS aos nomes dos campos no models.py (snake_case).

        nome = request.POST.get('nome')         # HTML: name="nome"
        cpf = request.POST.get('cpf')           # HTML: name="cpf"
        rg = request.POST.get('rg')             # HTML: name="rg"
        email = request.POST.get('email')       # HTML: name="email"
        telefone = request.POST.get('telefone') # HTML: name="telefone"
        cep = request.POST.get('cep')           # HTML: name="cep"
        rua = request.POST.get('rua')           # HTML: name="rua"
        descricao = request.POST.get('descricao') # HTML: name="descricao"

        # Crie a instância do Item usando os nomes de campo do seu models.py (snake_case)
        # e as variáveis locais correspondentes
        item = Item(
            nome=nome,
            cpf=cpf,
            rg=rg,
            email=email,
            telefone=telefone,
            cep=cep,
            rua=rua,
            descricao=descricao,
            # data_adesao é auto_now_add=True, NÃO passe aqui
        )
        try:
            item.save() # Se algum campo NOT NULL for None ou vazio (para CharField/EmailField), dará erro
            print("Item salvo com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar o item: {e}")
            # Você pode adicionar uma mensagem de erro para o usuário aqui
            # Por exemplo: return render(request, 'app/criar.html', {'error_message': 'Erro ao salvar. Verifique os campos obrigatórios.'})

    contexto = {
        'Itens': Item.objects.all()
    }
    return render(request, 'app/item.html', contexto)

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('cadastro')

# app/views.py

# app/views.py

def editar_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        print("Dados recebidos no POST (edicao):", request.POST) # <--- ADICIONE ESTA LINHA!

        item.nome = request.POST.get("nome")
        item.cpf = request.POST.get("cpf")
        item.rg = request.POST.get("rg")
        item.email = request.POST.get("email")
        item.telefone = request.POST.get("telefone")
        item.cep = request.POST.get("cep")
        item.rua = request.POST.get("rua")
        item.descricao = request.POST.get("descricao")
        # data_adesao NÃO é editável por aqui se for auto_now_add ou auto_now

        try:
            item.save()
            print("Item editado com sucesso!")
        except Exception as e:
            print(f"Erro ao editar o item: {e}")
            contexto_view = {
                'item': item,
                'error_message': f'Erro ao editar: {e}'
            }
            return render(request, 'app/editar.html', contexto_view)

        if 'salvar_retornar' in request.POST:
            return redirect('cadastro')
        else:
            return redirect('editar_item', id=item.id)

    contexto_view = {
        'item': item
    }
    return render(request, 'app/editar.html', contexto_view)