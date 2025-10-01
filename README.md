# 后端开发笔记

- 要建立这种在 apps 目录下包含多个应用（如 basic、goods、order、users）的 Django 项目结构，可按照以下步骤操作：

1. 准备 apps 目录
   在 Django 项目的根目录（与 manage.py 同目录）下，创建 apps 目录：

  ```c++
bash
mkdir apps
  ```


2. 配置 apps 目录为 Python 包
   进入 apps 目录，创建 __init__.py 文件，使其成为 Python 包：

  ```c++
bash
cd apps
touch __init__.py
  ```


3. 创建各应用
   使用 python manage.py startapp 命令在 apps 目录下创建应用。例如，创建 goods 应用：

  ```c++
bash
// 回到项目根目录
cd ..
python manage.py startapp goods apps/goods
同理，创建 basic、order、users 等应用：
bash
python manage.py startapp basic apps/basic
python manage.py startapp order apps/order
python manage.py startapp users apps/users
  ```

  



如果将应用（app）放在自定义的 apps 目录下，需要在 settings.py 中进行额外配置，确保 Django 能正确找到这些应用。具体配置方法如下：

1. 添加 apps 目录到 Python 路径
   在 settings.py 的开头，添加以下代码，将 apps 目录加入 Python 的模块搜索路径：

  ```python
import os
import sys

#项目根目录（manage.py 所在的目录）

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#将 apps 目录添加到 Python 路径

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 关键配置
  ```

使用 PyMySQL 时，Django 的数据库迁移操作和正常流程基本一致，但需要确保配置正确。以下是具体步骤和注意事项：

- 确认 PyMySQL 配置正确

首先确保已在项目中配置 PyMySQL 作为 MySQL 驱动，在项目根目录的 `__init__.py` 中添加：

```python
import pymysql
pymysql.install_as_MySQLdb()  # 关键：将 PyMySQL 伪装成 MySQLdb
```

- 执行迁移的步骤（和正常流程相同）

#### ① 生成迁移文件

```bash
# 为指定应用生成迁移（如 users 应用）
python manage.py makemigrations users

# 为所有应用生成迁移
python manage.py makemigrations
```

#### ② 应用迁移到数据库

```bash
python manage.py migrate
```

Django 关于模型主键类型的提示，主要原因是你的模型没有显式定义主键字段，Django 自动创建了默认的 `AutoField` 主键，而新版本的 Django 推荐显式配置主键类型。

解决方法很简单，只需在 `settings.py` 中添加一行配置，统一指定默认的主键类型即可：

```python
# 在 settings.py 中添加以下配置
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

## 关于media路径配置问题

已经正确配置了 MEDIA_URL 和 MEDIA_ROOT，这是 Django 处理媒体文件的基础设置：
MEDIA_URL = "/media/"：定义了媒体文件在 URL 中的访问前缀（例如访问路径会是 http://example.com/media/user_img/Screenshot-2.png）

MEDIA_ROOT = os.path.join(BASE_DIR, "media")：定义了媒体文件在服务器上的实际存储目录（与项目根目录下的 media 文件夹对应）

如果仍然出现 404 错误，建议从以下几个方面进一步排查：
开发环境路由配置如之前所说，开发环境需要在主 urls.py 中添加媒体文件的路由映射，确保开发服务器能正确处理媒体文件请求：

```python
# 主 urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


# 你的其他路由...
```

| 场景                                  | `path()` 写法（简洁）                        | `re_path()` 写法（更灵活）                                 |
| ------------------------------------- | -------------------------------------------- | ---------------------------------------------------------- |
| **固定 URL**                          | `path('about/', views.about)`                | `re_path(r'^about/$', views.about)`                        |
| **整型参数**                          | `path('blog/<int:year>/', views.blog)`       | `re_path(r'^blog/(?P<year>[0-9]+)/$', views.blog)`         |
| **字符串参数**（不含 `/`）            | `path('user/<str:name>/', views.user)`       | `re_path(r'^user/(?P<name>[^/]+)/$', views.user)`          |
| **slug 参数**（字母、数字、`-`、`_`） | `path('post/<slug:slug>/', views.post)`      | `re_path(r'^post/(?P<slug>[-a-zA-Z0-9_]+)/$', views.post)` |
| **UUID 参数**                         | `path('item/<uuid:uid>/', views.item)`       | `re_path(r'^item/(?P<uid>[0-9a-f-]{36})/$', views.item)`   |
| **路径参数**（可以含 `/`）            | `path('files/<path:subpath>/', views.files)` | `re_path(r'^files/(?P<subpath>.+)/$', views.files)`        |
| **可选参数**（path 不支持）           | ❌                                            | `re_path(r'^blog(?:/(?P<year>[0-9]{4}))?/$', views.blog)`  |
| **多种写法合并**                      | ❌                                            | `re_path(r'^(page                                          |
| **范围限制**（年份 2010–2025）        | ❌                                            | `re_path(r'^blog/(?P20(1[0-9]                              |
| **手机号格式**                        | ❌                                            | `re_path(r'^phone/(?P1(3                                   |
| **开头/结尾精确匹配**                 | ❌                                            | `re_path(r'^about$', views.about)`                         |
