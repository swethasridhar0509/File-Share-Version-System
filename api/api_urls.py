from django.urls import path, include
from . import api_views

urlpatterns = [
    path('files', api_views.files_view, name="files-list"),
    path('upload', api_views.file_upload, name="file-upload"),
    path('file/<int:id>/', include([path('', api_views.file_view, name="file-view"),
                                    path('upload', api_views.file_version_upload, name="version-upload"),
                                    path('versions', api_views.file_versions_view, name="file-versions"),
                                    path('share', api_views.file_share, name="file-share"),
                                    path('restore', api_views.file_restore, name="file-restore"),
                                    ]))
]