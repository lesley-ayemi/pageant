from home.models import Gallery
def gallery_posts(request):
    recent_gallery = Gallery.objects.all()
    return {'gallery_posts':Gallery.objects.all()} 