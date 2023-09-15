from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .models import Project
from django.urls import reverse_lazy

def list_projects(request):
    return render(
        request,
        "projects/project_list.html",
        {"projects": Project.objects.all(), "page_title": "Lista de Projetos"},
    )

class ProjectListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Lista de Projetos"
        return context

    def get_context_object_name(self, object_list):
        return "projects"



class ProjectCreateView(CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:list_projects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Criar Projeto"
        return context

class ProjectUpdateView(UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:list_projects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Editar Projeto"
        return context


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects:list_projects")
    return render(
        request,
        "projects/project_confirm_delete.html",
        {"page_title": "Deletar Projeto", "project": project},
    )


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(
        request,
        "projects/project_detail.html",
        {"page_title": "Detalhes do Projeto", "project": project},
    )


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("projects:list_projects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Deletar Projeto"
        return context

class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Detalhes do Projeto"
        return context