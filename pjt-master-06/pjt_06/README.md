>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 06

### 이번 pjt 를 통해 배운 내용

* 장고와 DB를 결합한 프로젝트를 처음 진행해보았습니다.
* 검색을 하지않고 모든 module과 코드를 작성하는 것이 쉽지않다는 것을 또 한 번 느꼈습니다.
* 구조를 파악하고 장고 안에서 읽어오는 방향성과 DB와의 연동 대한 중요성을 깨달았습니다.

## A. base.html

* 요구 사항 : 
* “공통 부모 템플릿”
• 로그인 상태
A. 회원정보수정
B. 로그아웃
C. 회원탈퇴
D. 내 프로필
• 비로그인 상태
A. 로그인
B. 회원가입

* 결과 : base.html에 user.is_authenticated를 통해 로그인한 경우와 아닌 경우를 나눠 주었습니다.
  
  * 문제 접근 방법 및 코드 설명
``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
    <div id="nav">
        {% if user.is_authenticated %}
        <h2 id="user-hello"><i>Hello, {{user}}</i></h2>
        <a href="{% url 'accounts:update' %}">회원정보수정</a>
          <a href="{% url 'accounts:logout' %}">로그아웃</a>
          <form action="{% url 'accounts:delete' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="회원탈퇴">
            <a href="{% url 'accounts:profile' user.username %}" id="movie-title">내 프로필</a>
          </form>
        {% else %}
        <a href="{% url 'accounts:login' %}">Login</a>
          <a href="{% url 'accounts:signup' %}">Signup</a>
        {% endif %}
      </div>
      
      <hr>
      <div id="content">
  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
</body>
</html>

```
* 이 문제에서 어려웠던점
  * 2주만에 장고를 다루면서 is_authenticated와 같은 것들에 대하여 기억을 하지 못해 추가적인 검색을 통해 필요한 부분을 알아내었습니다.
* 내가 생각하는 이 문제의 포인트
  * 다양한 기능에 대해 잘 기억하고 활용하는 것
  * settings에 user에 대한 정보를 받아오기 위한 한줄을 적어넣는 것

## B. index.html

* 요구 사항 : 
* “전체 영화 목록 조회 페이지”

* 결과 : 
* decorator(login_required / require_POST)을 사용하여 주소창을 통해 접근시 로그인을 안했을 떄 로그인 페이지로 갈 수 있게 만들었습니다.
  index.html에서 생성된 데이터의 title을 보여주며, title을 클릭할 시 detail.html로 pk와 함께 접근하도록 하였습니다.
* 문제 접근 방법 및 코드 설명

extends를 통해 로그인을 했다면 전체 영화 목록 데이터가 보이며 데이터별 title을 클릭하면 detail.html로 이동하게 만들었습니다.

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  {% if user.is_authenticated %}
  <a href="{% url 'movies:create' %}">[CREATE]</a>
  <hr>
  {% for movie in movies %}
    <a href="{% url 'movies:detail' movie.pk %}"><p>{{ movie.title }}</p></a>
    작성자: <a href="{% url 'accounts:profile' movie.user.username %}">{{movie.user}}</a>
    <div>
        <form action="{% url 'movies:likes' movie.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in movie.like_users.all %}
            <input type="submit" value="좋아요 취소">
            {% else %}
            <input type="submit" value="좋아요">
            {% endif %}
        </form>
    </div>

    <hr>
  {% endfor %}
  {% endif %}
{% endblock %}

```


* 이 문제에서 어려웠던점
  * views와 html에 app_name을 적을 때 's'를 빼먹는 경우가 있어 오류를 찾는데 오래걸렸습니다.
  * 데코레이터가 어떤 곳에서 import하는지 잘 몰라 애먹었습니다.
* 내가 생각하는 이 문제의 포인트
  * detail로 이동할 때 pk를 꼭 제공해주어야합니다.
  * 데코레이터의 중요성

## C. detail.html

* 요구 사항 : “영화 상세 정보 페이지”
• 특정 영화의 상세 정보를 표시합니다.
• 댓글을 작성할 수 있는 form을 표시합니다.
• 댓글 삭제 버튼은 댓글 작성자에게만 표시합니다.
• 해당 영화의 수정 및 삭제 버튼을 표시합니다.
• 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다

* 결과 : pk와 함께 전달되면 data의 title, description과 댓글이 보이도록 만들었습니다.
* 본인이 작성한 글이 아니라면 삭제 혹은 수정을 못하게 했습니다.
* 본인이 작성한 댓글이 아니라면 삭제 혹은 수정을 못하게 했습니다.
  
  * 문제 접근 방법 및 코드 설명

```html
{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <hr>
  <div>
    <h5>{{ movie.title }}</h5>
    <p>{{ movie.description }}</p>
</div>
<h5>댓글 목록</h5>
<hr><br>
<h5>Comments</h5>
<hr>
{% if comments %}
  <p><b>{{comments|length}}개의 댓글</b></p>
{% endif %}

<ul>
  {% for comment in comments %}
    <li>
      {{comment.content}} - {{comment.user}}
      {% if request.user == comment.user %}
        <form action="{% url 'movies:comments_delete' movie.pk comment.pk%}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% endif %}
    </li>
  {% empty %}
    <li>댓글이 없습니다</li>
  {% endfor %}
</ul>

{% if request.user.is_authenticated %}
    <form action="{% url 'movies:comments_create' movie.pk %}" method="POST">
    {% csrf_token %}
    {{comment_form}}
    <input type="submit" value="저장">
    </form>
{% else %}
    <a href="{% url 'accounts:login' %}">로그인이나하십쇼</a>
{% endif %}
{% if request.user == movie.user %}
<a href="{% url 'movies:update' movie.pk %}">UPDATE</a>
<a href="{% url 'movies:delete' movie.pk %}">DELETE</a>
<hr><br>
{% endif %}
<a href="{% url 'movies:index' %}">BACK</a>

{% endblock  %}

```

* 이 문제에서 어려웠던점
  * 정확한 app_name을 적어야 오류를 줄일 수 있습니다.
* 내가 생각하는 이 문제의 포인트
  * 같은 것을 적어야한다면 copy & paste를 하는 것이 오류를 줄이는데 도움이 됩니다..
  * request.user, comment.user과 movie.user 등을 잘 이용할 줄 알아야합니다.

## D. create.html

* 요구 사항 :
* “영화 생성 페이지”
• 특정 영화를 생성하기 위한 HTML form 요소를 표시합니다.
• 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
• 작성한 정보는 제출(submit)시 단일 영화 데이터를 저장하는
URL로 요청과 함께 전송됩니다.
• 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

* 결과
* form.as_p를 통해 forms.py에서 만들어둔 form을 계속 사용해주었고 영화에 대한 title과 description을 입력시 db에 포함되게 만들었습니다.


  * 문제 접근 방법 및 코드 설명

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
{% endblock %}

```

* 이 문제에서 어려웠던점
  * csrf를 빼먹으면 404 error가 나는 점을 잊지 말아야합니다.
* 내가 생각하는 이 문제의 포인트
  * 장고를 통해 data를 만들 때 꼭 csrf_token을 추가해줘야합니다.

## E. update.html

* 요구 사항 : 
*  “영화 수정 페이지”
• 특정 영화를 수정하기 위한 HTML form 요소를 표시합니다.
• 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
• HTML input 요소에는 기존 데이터를 출력합니다.
• Reset 버튼은 사용자의 모든 입력을 초기 값으로 재설정 합니다.
• 작성한 정보는 제출(submit)시 단일 영화 데이터를 수정하는
URL로 요청과 함께 전송됩니다.
• 영화 상세 정보 페이지(detail.html)로 이동하는 링크를 표시합니다

* 결과 : 
* data를 수정할 때 기존 data값이 무엇인지 나타내주었으며 reset시 기존의 데이터로 돌아갈 수 있게 만들었습니다.
* 본인 글이 아니라면 수정버튼 자체를 detail 페이지에서 막아뒀습니다.

  * 문제 접근 방법 및 코드 설명

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <hr>
  <form action="{% url 'movies:update' movie.pk %}" method="POST">
    {% csrf_token %}
    <div>
      <label for="title">TITLE</label>
      <input type="text" id="title" name="title" value="{{ movie.title }}">
    </div>
    <div>
      <label for="description">DESCRIPTION</label>
      <textarea id="description" rows="3" name="description">{{ movie.description }}</textarea>
    </div>
    <input type="reset" value="Reset">
    <button type="submit">Submit</button>
  </form>
  <hr>
  <a href="{% url 'movies:detail' movie.pk %}">BACK</a>
{% endblock %}

```

* 이 문제에서 어려웠던점
* html의 input type에 reset이 있다는 점을 몰랐어서 오래걸렸습니다.
* 내가 생각하는 이 문제의 포인트
* django를 할 때 html의 기본적인 것도 알아야한다.


## F. login.html

* 요구 사항 : 
* “로그인 페이지”
• 로그인을 위한 HTML form 요소를 표시합니다.
• 작성한 정보는 제출(submit)시 로그인 URL로 요청과 함께 전송됩니다.

* 결과 : 로그인 버튼을 누르면 로그인 페이지를 나오게 만들었습니다.

  * 문제 접근 방법 및 코드 설명

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="로그인">
  </form>
{% endblock content %}
```

* 이 문제에서 어려웠던점
* 앞서 영화 데이터를 생성할 때 처럼 꼭 csrf_token을 제공해주어야 에러가 나지 않습니다.
* 내가 생각하는 이 문제의 포인트
* csrf_token


## G. signup.html

* 요구 사항 : 
* “회원가입 페이지”
• 회원가입을 위한 HTML form 요소를 표시합니다.
• 작성한 정보는 제출(submit)시 회원가입 URL로 요청과 함께 전송됩니다.

* 결과 : 
* sign up을 누르면 회원가입 페이지로 이동합니다.

  * 문제 접근 방법 및 코드 설명

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="회원가입">
  </form>
  <a href="{% url 'movies:index' %}">목록보기</a>
{% endblock content %}

```

* 이 문제에서 어려웠던점
* method를 post인지 get인지 잘 지정해주어야합니다.
* 내가 생각하는 이 문제의 포인트
* form에서 url을 통해 이동할 때 method를 지정해주는 것의 중요성

## H. update.html

* 요구 사항 : 
* “회원정보수정 페이지”
• 회원정보수정을 위한 HTML form 요소를 표시합니다.
• 작성한 정보는 제출(submit)시 회원정보수정 URL로 요청과 함께 전송됩니다.

* 결과 : 
* 회원정보수정을 누를 시 회원정보를 수정할 수 있는 페이지로 이동합니다.

  * 문제 접근 방법 및 코드 설명

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="수정하기">
  </form>
  <a href="{% url 'movies:index' %}">목록보기</a>
{% endblock content %}

```

* 이 문제에서 어려웠던점
* 
* 내가 생각하는 이 문제의 포인트
* form.as_p는 정말 최고입니다.


## I. change_password.html

* 요구 사항 : 
* “비밀번호변경 페이지”
• 비밀번호변경 을 위한 HTML form 요소를 표시합니다.
• 작성한 정보는 제출(submit)시 비밀번호변경 URL로 요청과 함께 전송됩니다.

* 결과 : 
* 비밀번호 변경 페이지를 누르면 비밀번호 변경 페이지로 이동합니다.


  * 문제 접근 방법 및 코드 설명

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>비밀번호변경</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="변경하기">
  </form>
  <a href="{% url 'movies:index' %}">목록보기</a>
{% endblock content %}

```

* 이 문제에서 어려웠던점
* 
* 내가 생각하는 이 문제의 포인트
* form.as_p는 최고입니다.

-----

....

문제 푼 내용을 기반으로 적어주세요.

# 후기

* 2주만에 장고 프로젝트를 진행하면서 장고를 활용할 때 자동으로 로그인을 해주는 것과 같은 이미 존재하는 다양한 활용 import들을 얼마나 잘 쓰는 지에 대한 중요성을 느꼈습니다.
* 지난 주에 이어 장고 프로젝트에 DB 프로젝트를 추가하여 진행하였는데 DB와 장고 속 기본 테이블, 중계테이블이 어떻게 구성되며 어떤 FK, PK를 갖는지에 대해 한 번더 되새길 수 있는 시간이었습니다. 
* 이번 프로젝트를 하면서 2주밖에 쉬지 않았음에도 많은 부분들을 잊어 복습의 중요성을 다시 한 번 느끼게 되었습니다. 또한 필요한 것은 copy & paste가 오히려 에러를 줄일 수 있는 방법이라는 것을 알게 되었습니다.