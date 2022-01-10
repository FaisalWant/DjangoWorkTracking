from django.urls import path
from .views import PostCreateView, like_post, GeneralDetailPost, ProblemDetailPost,GeneralPostDelete

app_name="posts"

urlpatterns=[

	path('',PostCreateView.as_view(), name="post-list"),
	path('like/', like_post, name="post-like"),
	path('<pk>/detail/', GeneralDetailPost.as_view(), name="gp-detail"),
	path('<pk1>/<pk>/detail/', ProblemDetailPost.as_view(), name="pp-detail"),
	path('<pk>/delete/', GeneralPostDelete.as_view(), name="gp-delete"),
]





# pk1 --- Primary key of the Problem Post
# pk --- Primary key of the Problem reported

# while reporting -every time we reported problems and "checked" them as
# public, a problem post is added to the boarded (pk1). By pk we'll get the
# report 