from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Monster, Type
from .forms import BattleForm

# Create your views here.
# Monster Views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# View all monsters
@login_required
def monsters_index(request):
  monsters = Monster.objects.all() # Retrieve all monsters
  return render(request, 'monsters/index.html', {
    'monsters': monsters
  })

# View monster
@login_required
def monsters_detail(request, monster_id):
  monster = Monster.objects.get(id=monster_id)
  id_list = monster.types.all().values_list('id')
  types_monster_doesnt_have = Type.objects.exclude(id__in=id_list)
  battle_form = BattleForm()
  return render(request, 'monsters/detail.html', {
    'monster': monster, 'battle_form': battle_form,
    'types': types_monster_doesnt_have
  })

class MonsterCreate(LoginRequiredMixin, CreateView):
  model = Monster
  #fields = '__all__'
  fields = ['name', 'type', 'description', 'number']
  #success_url = '/monsters/{monster_id}'

  def form_valid(self, form):
   form.instance.user = self.request.user
   return super().form_valid(form)

class MonsterUpdate(LoginRequiredMixin, UpdateView):
  model = Monster
  fields = ['type', 'description', 'number']

class MonsterDelete(LoginRequiredMixin, DeleteView):
  model = Monster
  success_url = '/monsters'

# Battle Views

@login_required 
def add_battle(request, monster_id):
  form = BattleForm(request.POST)
  if form.is_valid():
    new_battle = form.save(commit=False)
    new_battle.monster_id = monster_id
    new_battle.save()
  return redirect('detail', monster_id=monster_id)

# Type Views

class TypeList(ListView):
  model = Type

class TypeDetail(DetailView):
  model = Type

class TypeCreate(CreateView):
  model = Type
  fields = '__all__'

class TypeUpdate(UpdateView):
  model = Type
  fields = ['name', 'weakness']

class TypeDelete(DeleteView):
  model = Type
  success_url = '/types'

@login_required
def assoc_type(request, monster_id, type_id):
  Monster.objects.get(id=monster_id).types.add(type_id)
  return redirect('detail', monster_id=monster_id)

@login_required
def unassoc_type(request, monster_id, type_id):
  Monster.objects.get(id=monster_id).types.remove(type_id)
  return redirect('detail', monster_id=monster_id)

# Sign Up View

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
