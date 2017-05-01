from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == "POST":
        import pdb; pdb.set_trace()  # breakpoint 722818ae //
        pass
    elif request.method == "GET":
        import pdb; pdb.set_trace()  # breakpoint b8ea18cb //
        return render(request, "login.html", {})
