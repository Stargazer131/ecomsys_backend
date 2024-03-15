# Generated by Django 4.1.13 on 2024-03-15 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('bio', models.TextField()),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'authors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'manufacturers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MobileType',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'mobile_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.IntegerField(blank=True, default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/product_images/')),
                ('type', models.CharField(choices=[('book', 'book'), ('clothes', 'clothes'), ('mobile', 'mobile')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'publishers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'styles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='product.product')),
                ('publish_year', models.IntegerField(blank=True, default=2020)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='product.author')),
            ],
            options={
                'db_table': 'books',
                'ordering': ['product__name'],
            },
        ),
        migrations.CreateModel(
            name='ClothingItem',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='product.product')),
                ('manufacturer_date', models.DateField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothing_items', to='product.manufacturer')),
            ],
            options={
                'db_table': 'clothes',
                'ordering': ['product__name'],
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='product.product')),
                ('release_date', models.DateField()),
                ('rom_size', models.IntegerField()),
                ('ram_size', models.IntegerField()),
                ('display_resolution', models.CharField(max_length=50)),
                ('battery_capacity', models.IntegerField()),
                ('chip', models.CharField(max_length=50)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobiles', to='product.manufacturer')),
                ('mobile_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobiles', to='product.mobiletype')),
            ],
            options={
                'db_table': 'mobiles',
                'ordering': ['product__name'],
            },
        ),
        migrations.CreateModel(
            name='ClothingItemStyle',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('style_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.style')),
                ('clothingitem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.clothingitem')),
            ],
            options={
                'db_table': 'clothes_styles',
            },
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='styles',
            field=models.ManyToManyField(through='product.ClothingItemStyle', to='product.style'),
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.genre')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.book')),
            ],
            options={
                'db_table': 'book_genres',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(through='product.BookGenre', to='product.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='product.publisher'),
        ),
    ]
