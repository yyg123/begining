from django import forms        #完成博客评论功能

class CommentForm(forms.Form):       #完成博客评论功能

    name=forms.CharField(label='称呼',max_length=16,error_messages={
        'required':'请填写您的称呼',
        'max_length':'称呼太长咯'
    })
    email=forms.EmailField(label='邮箱',error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式不正确'
    })
    content=forms.CharField(label='内容',error_messages={
        'required':'请填写您的评论内容!',
        'max_length':'评论内容太长咯'
    })