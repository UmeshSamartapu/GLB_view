Perfect — this is a **great project idea** 🔥 (and very useful for your AI + AR portfolio).

I’ll give you a **simple but complete Django project** that:

* ✅ Uploads `.glb` files
* ✅ Displays them
* ✅ Supports **Mobile AR + Laptop AR**
* ✅ Uses your exact features

---

# 🏗️ 1. Project Structure

```
glb_ar_project/
│
├── manage.py
├── db.sqlite3
│
├── glb_ar_project/
│   ├── settings.py
│   ├── urls.py
│
├── viewer/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│
├── templates/
│   ├── landing.html
│   ├── upload.html
│   ├── mobile.html
│   ├── laptop.html
│
├── media/
│   └── models/
│
├── static/
```

---

# ⚙️ 2. Install Requirements

```bash
pip install django
```

---

# 🚀 3. Create Project

```bash
django-admin startproject glb_ar_project
cd glb_ar_project
python manage.py startapp viewer
```

---

# ⚙️ 4. settings.py

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'

INSTALLED_APPS = [
    ...
    'viewer',
]
```

---

# 🧠 5. Model (Upload .glb)

### `viewer/models.py`

```python
from django.db import models

class GLBModel(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='models/')

    def __str__(self):
        return self.name
```

---

# 📝 6. Form

### `viewer/forms.py`

```python
from django import forms
from .models import GLBModel

class GLBUploadForm(forms.ModelForm):
    class Meta:
        model = GLBModel
        fields = ['name', 'file']
```

---

# 🧠 7. Views

### `viewer/views.py`

```python
from django.shortcuts import render, redirect
from .forms import GLBUploadForm
from .models import GLBModel

def landing(request):
    return render(request, 'landing.html')

def upload_model(request):
    if request.method == 'POST':
        form = GLBUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mobile')
    else:
        form = GLBUploadForm()
    return render(request, 'upload.html', {'form': form})

def mobile_view(request):
    model = GLBModel.objects.last()
    return render(request, 'mobile.html', {'model': model})

def laptop_view(request):
    model = GLBModel.objects.last()
    return render(request, 'laptop.html', {'model': model})
```

---

# 🌐 8. URLs

### `viewer/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('upload/', views.upload_model, name='upload'),
    path('mobile/', views.mobile_view, name='mobile'),
    path('laptop_ar/', views.laptop_view, name='laptop'),
]
```

### `glb_ar_project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('viewer.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

# 🎨 9. Templates

---

## 🏠 landing.html (Device Selection)

```html
<h1>🌸 AR Viewer</h1>

<a href="/mobile/">📱 Mobile AR</a><br><br>
<a href="/laptop_ar/">💻 Laptop AR</a><br><br>
<a href="/upload/">⬆ Upload Model</a>

<p>Mobile → needs HTTPS</p>
<p>Laptop → needs Hiro marker</p>
```

---

## 📤 upload.html

```html
<h2>Upload .glb Model</h2>

<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

---

## 📱 mobile.html (🔥 MAIN AR FEATURE)

```html
<script type="module"
src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<h2>📱 Mobile AR Viewer</h2>

{% if model %}
<model-viewer 
    src="{{ model.file.url }}"
    ar
    ar-modes="webxr scene-viewer quick-look"
    camera-controls
    auto-rotate
    shadow-intensity="1"
    style="width:100%; height:80vh;"
>
    <button slot="ar-button">🚀 Activate AR</button>
</model-viewer>
{% else %}
<p>No model uploaded</p>
{% endif %}
```

---

## 💻 laptop.html (🔥 MARKER AR)

```html
<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
<script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script>

<div style="position:absolute; top:10px;">
    <p>Point camera at Hiro Marker</p>
    <a href="https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png" target="_blank">
        Download Marker
    </a>
</div>

<a-scene embedded arjs="sourceType: webcam;">
    <a-assets>
        {% if model %}
        <a-asset-item id="model" src="{{ model.file.url }}"></a-asset-item>
        {% endif %}
    </a-assets>

    <a-marker preset="hiro">
        <a-entity 
            gltf-model="#model"
            scale="0.3 0.3 0.3"
            animation="property: rotation; to: 0 360 0; loop: true; dur: 8000">
        </a-entity>
    </a-marker>

    <a-entity camera></a-entity>
</a-scene>
```

```python
# glb_ar_project/settings.py

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # ✅ ADD THIS
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

---

# 🗄️ 10. Run Project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

# 🎯 Final Features (You Achieved ✅)

✔ Upload `.glb` files
✔ Mobile AR (WebXR + model-viewer)
✔ Laptop AR (Marker-based)
✔ 3D interaction (zoom, rotate)
✔ Real-time camera AR
✔ Animated models
✔ Clean UI navigation

---

Nice 🔥 — adding a **base + navbar + sidebar** will make your project look like a real professional system.

I’ll give you a **simple reusable layout** you can plug into your project.

---

# 🧱 1. Create `base.html`

📁 `templates/base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>GLB AR System</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        /* Navbar */
        .navbar {
            background-color: #2c3e50;
            color: white;
            padding: 15px;
            font-size: 18px;
        }

        /* Layout */
        .container {
            display: flex;
        }

        /* Sidebar */
        .sidebar {
            width: 220px;
            background-color: #34495e;
            height: 100vh;
            padding-top: 20px;
        }

        .sidebar a {
            display: block;
            color: white;
            padding: 12px;
            text-decoration: none;
        }

        .sidebar a:hover {
            background-color: #1abc9c;
        }

        /* Content */
        .content {
            flex: 1;
            padding: 20px;
        }
    </style>
</head>

<body>

<!-- 🔝 NAVBAR -->
<div class="navbar">
    🌸 GLB AR Viewer System
</div>

<div class="container">

    <!-- 📚 SIDEBAR -->
    <div class="sidebar">
        <a href="/">🏠 Home</a>
        <a href="/upload/">⬆ Upload Model</a>
        <a href="/mobile/">📱 Mobile AR</a>
        <a href="/laptop_ar/">💻 Laptop AR</a>
    </div>

    <!-- 📄 MAIN CONTENT -->
    <div class="content">
        {% block content %}
        {% endblock %}
    </div>

</div>

</body>
</html>
```

---

# 🏠 2. Update `landing.html`

```html
{% extends 'base.html' %}

{% block content %}

<h2>🌸 Welcome to AR Viewer</h2>

<p>Select a mode from sidebar 👈</p>

<ul>
    <li>📱 Mobile AR → Real world viewing</li>
    <li>💻 Laptop AR → Marker based</li>
</ul>

{% endblock %}
```

---

# 📤 3. Update `upload.html`

```html
{% extends 'base.html' %}

{% block content %}

<h2>Upload .glb Model</h2>

<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>

{% endblock %}
```

---

# 📱 4. Update `mobile.html`

```html
{% extends 'base.html' %}

{% block content %}

<script type="module"
src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<h2>📱 Mobile AR Viewer</h2>

{% if model %}
<model-viewer 
    src="{{ model.file.url }}"
    ar
    camera-controls
    auto-rotate
    shadow-intensity="1"
    style="width:100%; height:70vh;"
>
    <button slot="ar-button">🚀 Activate AR</button>
</model-viewer>
{% else %}
<p>No model uploaded</p>
{% endif %}

{% endblock %}
```

---

# 💻 5. Update `laptop.html`

```html
{% extends 'base.html' %}

{% block content %}

<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
<script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script>

<h2>💻 Laptop AR Viewer</h2>

<p>Point camera at Hiro Marker</p>

<a href="https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png" target="_blank">
    Download Marker
</a>

<a-scene embedded arjs="sourceType: webcam;">
    <a-assets>
        {% if model %}
        <a-asset-item id="model" src="{{ model.file.url }}"></a-asset-item>
        {% endif %}
    </a-assets>

    <a-marker preset="hiro">
        <a-entity 
            gltf-model="#model"
            scale="0.3 0.3 0.3"
            animation="property: rotation; to: 0 360 0; loop: true; dur: 8000">
        </a-entity>
    </a-marker>

    <a-entity camera></a-entity>
</a-scene>

{% endblock %}
```

---

# 🎯 6. What You Achieved Now

✅ Navbar (top header)
✅ Sidebar navigation
✅ Clean layout
✅ Reusable template (`base.html`)
✅ Professional UI structure

---

# 🧠 Simple Understanding

👉 Now your app works like:

```
Base Layout
   ├── Navbar
   ├── Sidebar
   └── Page Content (dynamic)
```

---



---


