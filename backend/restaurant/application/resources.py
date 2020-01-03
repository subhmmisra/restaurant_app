from import_export import resources
from application.models import *
from import_export.fields import Field


class RestaurantResource(resources.ModelResource):
    res_id = Field(attribute='res_id', column_name='Restaurant ID')
    res_nanme = Field(attribute='res_name', column_name='Restaurant Name')
    cuisines = Field(attribute='cuisines', column_name='Cuisines')
    avg_cost_two = Field(attribute='avg_cost_two',
                         column_name='Average Cost for two')
    currentcy = Field(attribute='currency', column_name='Currency')
    has_booking = Field(attribute='has_booking',
                        column_name='Has Table booking')
    has_online = Field(attribute='has_online_delivery',
                       column_name='Has Online delivery')
    aggregate_rating = Field(attribute='aggregate_rating',
                             column_name='Aggregate rating')
    rating_color = Field(attribute='rating_color', column_name='Rating color')
    rating_text = Field(attribute='rating_text', column_name='Rating text')
    votes = Field(attribute='votes', column_name='Votes')

    class Meta:
        model = Restaurant
        exclude = ('id', )
        import_id_fields = []
        fields = ('')
