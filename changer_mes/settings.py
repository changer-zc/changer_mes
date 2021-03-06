"""
Django settings for changer_mes project.

Generated by 'django-admin startproject' using Django 2.1.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import pymysql
from pathlib import Path
from django.contrib import admin
import simpleui
import django.core.exceptions
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@6w!t0ea)^0(9!4++3xjb122r4jk9yye9rqjwjtapdf%_2_$kp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'mes',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

IMPORT_EXPORT_USE_TRANSACTIONS = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'changer_mes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')]
        ,
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

WSGI_APPLICATION = 'changer_mes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mes',
        'USER':'changer',
        'PASSWORD':'wajy52111',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR,'/static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


admin.AdminSite.site_header="NEXRAY生产管理系统"
admin.AdminSite.site_title="NEXRAY"

SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = False
import time
import mes
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['业务订单','生产','IQC', '维修','库房', '用户管理','综合页面','测试'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': False,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [

        # {
        #     'name': '质检',
        #     'icon': 'fas fa-code',
        #     'models': [{
        #         'name': '质检记录',
        #         'url': 'http://www.baidu.com',
        #         'icon': 'far fa-surprise'
        #     },

#维修
        {
            'name': '维修',
            'icon': 'fas fa-tools',
            'models': [{
                'name': '维修记录',
                'url': 'mes/repair/',
                'icon': 'fas fa-tools'
            },
                {
                    'name': '维修治具记录',
                    'url': 'mes/tools_record/',
                    'icon': 'fas fa-tools'
                },
                {
                    'name': '维修报废记录',
                    'url': 'mes/repair_scrap/',
                    'icon': 'fas fa-tools'
                },

            ]
        },
#质检
        {
            'name': 'IQC',
            'icon': 'far fa-check-circle',
            'models': [{
                'name': '来料质检',
                'url': 'mes/iqc/',
                'icon': 'far fa-check-circle'
            },
                {
                    'name': '生产不良记录',
                    'url': 'mes/production_iqc/',
                    'icon': 'far fa-check-circle'
                },
                {
                    'name': '出货质检',
                    'url': 'mes/out_iqc/',
                    'icon': 'far fa-check-circle'
                },
                {
                    'name': '报表分析',
                    'url': 'mes/iqc/',
                    'icon': 'far fa-check-circle'
                },

            ]
        },
#用户管理
                {
                    'name': '用户管理',
                    'icon': 'fas fa-users',
                    'models': [

                        {
                            'name': '用户',
                            'url': '/admin/auth/user/',
                            'icon': 'fas fa-users'
                        },
                    ]
                },
#生产
        {
            'name': '生产',
            'icon': 'fas fa-gavel',
            'models': [{
                'name': '组装',
                'url': 'http://10.130.1.16:8000/add1/',
                'icon': 'fas fa-gavel'
            },
                {
                    'name': '基测',
                    'url': 'http://127.0.0.1:8000/add1',
                    'icon': 'fas fa-gavel'
                },
                {
                    'name': '烧机',
                    'url': 'http://127.0.0.1:8000/add1',
                    'icon': 'fas fa-gavel'
                },
                {
                    'name': '功测',
                    'url': 'http://127.0.0.1:8000/add1',
                    'icon': 'fas fa-gavel'
                },
                {
                    'name': '包装',
                    'url': 'http://127.0.0.1:8000/add1',
                    'icon': 'fas fa-gavel'
                },
                {
                    'name': '版本维护',
                    'url': 'mes/version_manager/',
                    'icon': 'fas fa-gavel'
                },
                {
                    'name': '报表分析',
                    'url': 'http://127.0.0.1:8000/add1',
                    'icon': 'fas fa-gavel'
                },

            ]
        },
#业务订单
        {
            'name': '业务订单',
            'icon': 'fas fa-american-sign-language-interpreting',
            'models': [{
                'name': '生产询期',
                'url': 'mes/repair/',
                'icon': 'fas fa-american-sign-language-interpreting'
            },
                {
                    'name': '生产询料',
                    'url': 'mes/repair/',
                    'icon': 'fas fa-american-sign-language-interpreting'
                },
                {
                    'name': '录入订单/通知各部',
                    'url': 'mes/repair/',
                    'icon': 'fas fa-american-sign-language-interpreting'
                },

            ]
        },

#库房

        {
            'name': '库房',
            'icon': 'fas fa-warehouse',
            'models': [{
                'name': '盘点',
                'url': 'http://127.0.0.1:8000/add1',
                'icon': 'fas fa-warehouse'
            },
                {
                    'name': '入库记录',
                    'url': 'mes/in_record',
                    'icon': 'fas fa-warehouse'
                },
                {
                    'name': '出库记录',
                    'url': 'mes/out_record',
                    'icon': 'fas fa-warehouse'
                },
                {
                    'name': '库存',
                    'url': 'mes/ware_house',
                    'icon': 'fas fa-warehouse'
                },


            ]
        },


        {
            'name': '综合页面',
            'url': '/test02/',
            'icon': 'fas fa-users'
        },



        #测试
        {
            'name': '测试',
            'icon': 'fas fa-warehouse',
            'models': [{
                'name': '测试',
                'url': 'mes/test',
                'icon': 'fas fa-warehouse'
            },]

        }




            ]
        }






