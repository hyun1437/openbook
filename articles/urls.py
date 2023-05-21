from django.urls import path
from articles import views


urlpatterns = [    
    path('', views.ArticleView.as_view(), name='article_view'),
    path('feed/', views.FeedView.as_view(), name='feed_view'), # 피드 페이지
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail_view'), # 게시글 상세페이지
    path('<int:article_id>/comment/', views.CommentView.as_view(), name='comment_view'), # 댓글
    path('<int:article_id>/comment/<int:comment_id>', views.CommentView.as_view(), name='comment_view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='like_view'), # 좋아요
]