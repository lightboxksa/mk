from django.shortcuts import redirect


# defualt view
def start(request, exception=None):
  return redirect('/dashboard')

# page not found
def page_not_found_view(request, exception=None):
  return redirect('/dashboard')

# error view
def error_view(request, exception=None):
  return redirect('/dashboard')

# permission denied
def permission_denied_view(request, exception=None):
  return redirect('/dashboard')

# ad request
def ad_request_view(request, exception=None):
  return redirect('/dashboard')
