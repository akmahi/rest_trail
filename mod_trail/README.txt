Data integrity Options
https://www.webforefront.com/django/setuprelationshipsdjangomodels.html

*on_delete*

1.models.CASECADE(default)
    delete related(foreign key pointing table) data while deleted
2.models.PROTECTED
    prevent to delete data(foreign key pointing table)
3.models.SET_NULL
    While foreign key pointing data delete, set null on foreign key present table
    * Before setting this add null = True on Foreign key feild
4.models.SET_DEFAULT
    While foreign key pointing data delete, default value assigned to this
    * Before setting this add default option on Foreign key feild
5.models.SET
    Assign value while delete
6.models.DO_NOTHING
    No action is taken when related records are removed. This is generally a bad relational database practice.

Reverse Relationship

_set
    used to establis reverse relation
    EX:
    country.Objects.filter(City ='') -1
    City.item_set.all()-2

    Both provide asame o/p

related_name
    using this to rename the reverse relation and disable the reverse relation
    change name
        model.ForeignKey(... related_name = 'cty')
        Then above query like
        City.cty_set.all()-2

related_query_name
    using this override the related_name name
    models.ForeignKey(...related_name='cty',related_query_name='ctystart')

    #Direct access, Item records with price higher than 1
    Items.objects.filter(price__gt=1)

    # Reverse access query, Menu records with Item price higher than 1
    Menu.objects.filter(item__price__gt=1)

    While use related_name above query like
    menu.Object.filter(cty__price__gt=1)

    While use related_query_name for above query like
    menu.Object.filter(ctystart__price__gt=1)