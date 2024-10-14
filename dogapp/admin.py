from django.contrib import admin
from .models import Dog, Breed

# Admin configuration for the Breed model
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')
    search_fields = ('name',)  # Allow search by breed name

# Admin configuration for the Dog model
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'get_owner', 'gender', 'color', 'favoritefood', 'favoritetoy')
    search_fields = ('name', 'breed__name')  # Allow search by dog name and breed name
    list_filter = ('age', 'breed', 'owner', 'gender', 'color')  # Add filters for easier browsing
    list_display_links = ('name',)
    fields = ('owner', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy')

    def get_owner(self, obj):
        """Displays the owner's username (assuming owner is a ForeignKey to the User model)"""
        return obj.owner.username  # If owner is a ForeignKey, access its username

    get_owner.short_description = 'Owner'  # Set the column label for owner

# Register the models to appear in the Django admin interface
admin.site.register(Breed, BreedAdmin)
admin.site.register(Dog, DogAdmin)
