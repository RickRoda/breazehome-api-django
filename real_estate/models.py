from django.conf import settings
from django.db import models
from django.contrib.gis.db import models as gis_models
import user.models
from django.utils import timezone


class Agent(models.Model):
    agent_status = models.CharField(
        max_length=200,
        null=True
    )
    agent_type = models.CharField(
        max_length=200,
        null=True
    )
    board = models.CharField(
        max_length=200,
        null=True
    )
    cellphone = models.CharField(
        max_length=20,
        null=True
    )
    direct_work_phone = models.CharField(
        max_length=20,
        null=True
    )
    email = models.CharField(
        max_length=50,
        null=True
    )
    fax_phone = models.CharField(
        max_length=20,
        null=True
    )
    first_name = models.CharField(
        max_length=25,
        null=True
    )
    full_name = models.CharField(
        max_length=50,
        null=True
    )
    generational_name = models.CharField(
        max_length=50,
        null=True
    )
    home_phone = models.CharField(
        max_length=20,
        null=True
    )
    is_deleted = models.NullBooleanField(
        null=True
    )
    last_name = models.CharField(
        max_length=20,
        null=True
    )
    license_number = models.CharField(
        max_length=50,
        null=True
    )
    mail_address = models.CharField(
        max_length=50,
        null=True
    )
    mail_care_of = models.CharField(
        max_length=200,
        null=True
    )
    mail_city = models.CharField(
        max_length=50,
        null=True
    )
    mail_postal_code = models.CharField(
        max_length=15,
        null=True
    )
    mail_or_state_province = models.CharField(
        max_length=50,
        null=True
    )
    matrix_modified_dt = models.CharField(
        max_length=200,
        null=True
    )
    matrix_testing = models.CharField(
        max_length=50,
        null=True
    )
    matrix_unique_id = models.CharField(
        max_length=30,
        null=True
    )
    matrix_user_type = models.CharField(
        max_length=50,
        null=True
    )
    member_code = models.CharField(
        max_length=100,
        null=True
    )
    middle_name = models.CharField(
        max_length=50,
        null=True
    )
    mls = models.CharField(
        max_length=100,
        null=True
    )
    mlsid = models.CharField(
        max_length=100,
        null=True
    )
    muc = models.CharField(
        max_length=100,
        null=True
    )
    office_mls_id = models.CharField(
        max_length=50,
        null=True
    )
    office_mui = models.CharField(
        max_length=100,
        null=True
    )
    password = models.CharField(
        max_length=50,
        null=True
    )
    provider_key = models.CharField(
        max_length=50,
        null=True
    )
    provider_modification_timestamp = models.CharField(
        max_length=50,
        null=True
    )
    rets_office_visibility = models.CharField(
        max_length=50,
        null=True
    )
    ruc = models.CharField(
        max_length=50,
        null=True
    )
    web_address = models.CharField(
        max_length=255,
        null=True
    )

class OpenHouse(models.Model):
    active_yn = models.NullBooleanField(
        null=True
    )
    description = models.CharField(
        max_length=1000,
        null=True
    )
    end_time = models.CharField(
        max_length=50,
        null=True
    )
    entry_order = models.CharField(
        max_length=50,
        null=True
    )
    is_deleted = models.NullBooleanField(
        null=True
    )
    listing_mui = models.BigIntegerField(
        null=True
    )
    matrix_modified_dt = models.DateTimeField(
        null=True
    )
    matrix_unique_id = models.CharField(
        max_length=30,
        null=True
    )
    open_house_date = models.DateTimeField(
        null=True
    )
    open_house_type = models.CharField(
        max_length=50,
        null=True
    )
    provider_key = models.CharField(
        max_length=200,
        null=True
    )
    refreshments = models.CharField(
        max_length=5,
        null=True
    )
    start_time = models.CharField(
        max_length=50,
        null=True
    )


class Property(models.Model):
    address_internet_display = models.CharField(
        max_length=200,
        null=True
    )
    auction_type = models.CharField(
        max_length=200,
        null=True
    )
    auction_yn = models.NullBooleanField(
        null=True
    )
    available_date = models.DateTimeField(
        null=True
    )
    balcony_porchandor_patio_yn = models.NullBooleanField(
        null=True
    )
    baths_full = models.IntegerField(
        null=True
    )
    baths_half = models.IntegerField(
        null=True
    )
    beds_total = models.IntegerField(
        null=True
    )
    broker_remarks = models.CharField(
        max_length=200,
        null=True
    )
    building_number = models.CharField(
        max_length=200,
        null=True
    )
    cable_available_yn = models.NullBooleanField(
        null=True
    )
    city = models.CharField(
        max_length=200,
        null=True
    )
    close_date = models.DateTimeField(
        null=True
    )
    close_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True
    )
    count = models.IntegerField(
        default = 0
    )
    current_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True
    )
    efficiency_yn = models.NullBooleanField(
        null=True
    )
    electric_service = models.CharField(
        max_length=200,
        null=True
    )
    exterior_features = models.CharField(
        max_length=200,
        null=True
    )
    for_lease_yn = models.NullBooleanField(
        null=True
    )
    for_sale_yn = models.NullBooleanField(
        null=True
    )
    housing_older_persons_act = models.CharField(
        max_length=200,
        null=True
    )
    idx_opt_in_yn = models.NullBooleanField(
        null=True
    )
    internet_yn = models.NullBooleanField(
        null=True
    )
    is_deleted = models.NullBooleanField(
        null=True
    )
    joint_agency_yn = models.NullBooleanField(
        null=True
    )
    lease_expiration_date = models.DateTimeField(
        null=True
    )
    lease_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True
    )
    location = models.CharField(
        max_length=200,
        null=True
    )
    location_point = gis_models.PointField(
        null=True
    )
    location_level = models.CharField(
        max_length=60,
        null=True
    )
    locationof_property = models.CharField(
        max_length=200,
        null=True
    )
    lot_description = models.CharField(
        max_length=200,
        null=True
    )
    lotor_track_num = models.CharField(
        max_length=200,
        null=True
    )
    lot_sq_footage = models.IntegerField(
        null=True
    )
    map_coordinates = models.CharField(
        max_length=200,
        null=True
    )
    matrix_unique_id = models.BigIntegerField(
        null=True,
        unique=True
    )
    parking_space_number = models.CharField(
        max_length=200,
        null=True
    )
    patio_balcony_dimensions = models.CharField(
        max_length=200,
        null=True
    )
    pets_allowed_yn = models.NullBooleanField(
        null=True
    )
    pool_yn = models.NullBooleanField(
        null=True
    )
    postal_code = models.CharField(
        max_length=200,
        null=True
    )
    postal_code_plus4 = models.CharField(
        max_length=200,
        null=True
    )
    property_detached_yn = models.NullBooleanField(
        null=True
    )
    property_sq_ft = models.IntegerField(
        null=True
    )
    property_sub_type = models.CharField(
        max_length=200,
        null=True
    )
    property_type = models.CharField(
        max_length=200,
        null=True
    )
    property_type_information = models.CharField(
        max_length=200,
        null=True
    )
    prop_type_typeof_building = models.CharField(
        max_length=200,
        null=True
    )
    ready_to_activate_yn = models.NullBooleanField(
        null=True
    )
    real_estate_taxes = models.IntegerField(
        null=True
    )
    renewable_rental_yn = models.NullBooleanField(
        null=True
    )
    rent_period = models.CharField(
        max_length=200,
        null=True
    )
    room_count = models.IntegerField(
        null=True
    )
    separate_meter_yn = models.NullBooleanField(
        null=True
    )
    short_sale_yn = models.NullBooleanField(
        null=True
    )
    sq_ft_total = models.IntegerField(
        null=True
    )
    state_or_province = models.CharField(
        max_length=200,
        null=True
    )
    status = models.CharField(
        max_length=200,
        null=True
    )
    status_change_timestamp = models.DateTimeField(
        null=True
    )
    thumbnail_path = models.CharField(
        max_length=200,
        unique=True,
        null=True,
        blank=True
    )
    total_acreage = models.DecimalField(
        max_digits=26,
        decimal_places=8,
        null=True
    )
    total_mortgage = models.IntegerField(
        null=True
    )
    total_units = models.IntegerField(
        null=True
    )
    year_built = models.IntegerField(
        null=True
    )
    zoning_information = models.CharField(
        max_length=200,
        null=True
    )
    open_house_upcoming = models.CharField(
        max_length=200,
        null=True
    )


    objects = gis_models.GeoManager()
    class Meta:
        verbose_name_plural = "properties"

class FavProperty(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        null=True

    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        null=True

    )

    class Meta:
        unique_together = ('user', 'property')
        verbose_name_plural = "favproperties"

class Board(models.Model):
    name = models.CharField(
        max_length=200,
        null=True
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        null=True

    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        null=True

    )


    class Meta:
        unique_together = ('name', 'property')
        verbose_name_plural = "boards"




class PropertyDetail(models.Model):
    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE
    )
    accountingand_legal_expens = models.CharField(
        max_length=200,
        null=True
    )
    a_c_percentage = models.CharField(
        max_length=200,
        null=True
    )
    acreage_description = models.CharField(
        max_length=200,
        null=True
    )
    active_open_house_count = models.CharField(
        max_length=200,
        null=True
    )
    additional_business_names = models.CharField(
        max_length=200,
        null=True
    )
    additional_furnished_info = models.CharField(
        max_length=200,
        null=True
    )
    addl_move_in_cost_yn = models.CharField(
        max_length=200,
        null=True
    )
    address_internet_display = models.CharField(
        max_length=200,
        null=True
    )
    addresson_internet = models.CharField(
        max_length=200,
        null=True
    )
    adjusted_area_sf = models.CharField(
        max_length=200,
        null=True
    )
    a_dom = models.CharField(
        max_length=200,
        null=True
    )
    advertising_expenses = models.CharField(
        max_length=200,
        null=True
    )
    agent_alternate_phone = models.CharField(
        max_length=200,
        null=True
    )
    agent_license_num = models.CharField(
        max_length=200,
        null=True
    )
    agents_office_extension = models.CharField(
        max_length=200,
        null=True
    )
    amenities = models.CharField(
        max_length=200,
        null=True
    )
    annual_base_rate = models.CharField(
        max_length=200,
        null=True
    )
    application_fee = models.CharField(
        max_length=200,
        null=True
    )
    approval_information = models.CharField(
        max_length=200,
        null=True
    )
    approximate_lot_size = models.CharField(
        max_length=200,
        null=True
    )
    approx_sqft_total_area = models.CharField(
        max_length=200,
        null=True
    )
    area = models.CharField(
        max_length=200,
        null=True
    )
    assoc_fee_paid_per = models.CharField(
        max_length=200,
        null=True
    )
    association_fee = models.CharField(
        max_length=200,
        null=True
    )
    assumable_chattel_balance = models.CharField(
        max_length=200,
        null=True
    )
    assumable_yn = models.CharField(
        max_length=200,
        null=True
    )
    available_documents = models.CharField(
        max_length=200,
        null=True
    )
    a_vm = models.CharField(
        max_length=200,
        null=True
    )
    baths_total = models.CharField(
        max_length=200,
        null=True
    )
    bedroom_description = models.CharField(
        max_length=200,
        null=True
    )
    blogging = models.CharField(
        max_length=200,
        null=True
    )
    board_identifier = models.CharField(
        max_length=200,
        null=True
    )
    boat_dock_accommodates = models.CharField(
        max_length=200,
        null=True
    )
    brand_name = models.CharField(
        max_length=200,
        null=True
    )
    building_area_alternative = models.CharField(
        max_length=200,
        null=True
    )
    building_area_alt_source = models.CharField(
        max_length=200,
        null=True
    )
    building_includes = models.CharField(
        max_length=200,
        null=True
    )
    building_name_number = models.CharField(
        max_length=200,
        null=True
    )
    buyer_countryof_residence = models.CharField(
        max_length=200,
        null=True
    )
    buyers_zip_code = models.CharField(
        max_length=200,
        null=True
    )
    cancelled_date = models.CharField(
        max_length=200,
        null=True
    )
    carport_description = models.CharField(
        max_length=200,
        null=True
    )
    c_dom = models.CharField(
        max_length=200,
        null=True
    )
    c_dom_change_notes = models.CharField(
        max_length=200,
        null=True
    )
    c_dom_initial = models.CharField(
        max_length=200,
        null=True
    )
    ceiling_description = models.CharField(
        max_length=200,
        null=True
    )
    ceiling_height = models.CharField(
        max_length=200,
        null=True
    )
    city = models.CharField(
        max_length=200,
        null=True
    )
    co_agent_license_num = models.CharField(
        max_length=200,
        null=True
    )
    co_list_agent_mui = models.CharField(
        max_length=200,
        null=True
    )
    co_list_agent_direct_work_phone = models.CharField(
        max_length=200,
        null=True
    )
    co_list_agent_email = models.CharField(
        max_length=200,
        null=True
    )
    co_list_agent_full_name = models.CharField(
        max_length=200,
        null=True
    )
    co_list_agent_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    co_list_office_mui = models.CharField(
        max_length=200,
        null=True
    )
    co_list_office_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    co_list_office_name = models.CharField(
        max_length=200,
        null=True
    )
    co_list_office_phone = models.CharField(
        max_length=200,
        null=True
    )
    column_description = models.CharField(
        max_length=200,
        null=True
    )
    common_area_maint_amount = models.CharField(
        max_length=200,
        null=True
    )
    common_area_maint_includes = models.CharField(
        max_length=200,
        null=True
    )
    complex_name = models.CharField(
        max_length=200,
        null=True
    )
    comprehensive_plan_use = models.CharField(
        max_length=200,
        null=True
    )
    compto_buyers_agent = models.CharField(
        max_length=200,
        null=True
    )
    compto_non_representative = models.CharField(
        max_length=200,
        null=True
    )
    compto_transaction_broker = models.CharField(
        max_length=200,
        null=True
    )
    conditional_date = models.CharField(
        max_length=200,
        null=True
    )
    construction_type = models.CharField(
        max_length=200,
        null=True
    )
    convertible_bedroom_yn = models.CharField(
        max_length=200,
        null=True
    )
    cooling_description = models.CharField(
        max_length=200,
        null=True
    )
    co_sell_agent_license_num = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_agent_mui = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_agent_direct_work_phone = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_agent_email = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_agent_full_name = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_agent_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_office_mui = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_office_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_office_name = models.CharField(
        max_length=200,
        null=True
    )
    co_selling_office_phone = models.CharField(
        max_length=200,
        null=True
    )
    costof_sales = models.CharField(
        max_length=200,
        null=True
    )
    county_land_code = models.CharField(
        max_length=200,
        null=True
    )
    county_or_parish = models.CharField(
        max_length=200,
        null=True
    )
    current_price = models.CharField(
        max_length=200,
        null=True
    )
    dade_assessed_amt_soh_value = models.CharField(
        max_length=200,
        null=True
    )
    dade_market_amt_assessed_amt = models.CharField(
        max_length=200,
        null=True
    )
    days_open = models.CharField(
        max_length=200,
        null=True
    )
    decal_number = models.CharField(
        max_length=200,
        null=True
    )
    deed_restrictions = models.CharField(
        max_length=200,
        null=True
    )
    den_dimensions = models.CharField(
        max_length=200,
        null=True
    )
    deposit_information = models.CharField(
        max_length=200,
        null=True
    )
    design = models.CharField(
        max_length=200,
        null=True
    )
    design_description = models.CharField(
        max_length=200,
        null=True
    )
    development = models.CharField(
        max_length=200,
        null=True
    )
    development_name = models.CharField(
        max_length=200,
        null=True
    )
    dining_area_dimensions = models.CharField(
        max_length=200,
        null=True
    )
    dining_description = models.CharField(
        max_length=200,
        null=True
    )
    dining_room_dimensions = models.CharField(
        max_length=200,
        null=True
    )
    directions = models.CharField(
        max_length=200,
        null=True
    )
    dock_height = models.CharField(
        max_length=200,
        null=True
    )
    dock_information = models.CharField(
        max_length=200,
        null=True
    )
    dock_number = models.CharField(
        max_length=200,
        null=True
    )
    d_om = models.CharField(
        max_length=200,
        null=True
    )
    door_height = models.CharField(
        max_length=200,
        null=True
    )
    d_xoriglpid = models.CharField(
        max_length=200,
        null=True
    )
    d_xorigmlno = models.CharField(
        max_length=200,
        null=True
    )
    d_xorigmlsid = models.CharField(
        max_length=200,
        null=True
    )
    d_xorigoffcode = models.CharField(
        max_length=200,
        null=True
    )
    eave_height = models.CharField(
        max_length=200,
        null=True
    )
    e_bh_submit_offer = models.CharField(
        max_length=200,
        null=True
    )
    efficiency_yn = models.CharField(
        max_length=200,
        null=True
    )
    electric_service = models.CharField(
        max_length=200,
        null=True
    )
    elementary_school = models.CharField(
        max_length=200,
        null=True
    )
    elevation_above_sea_level = models.CharField(
        max_length=200,
        null=True
    )
    environmental_audit = models.CharField(
        max_length=200,
        null=True
    )
    equipment_appliances = models.CharField(
        max_length=200,
        null=True
    )
    exclude_from_inventory_stats = models.CharField(
        max_length=200,
        null=True
    )
    expected_closing_date = models.CharField(
        max_length=200,
        null=True
    )
    expense_amount = models.CharField(
        max_length=200,
        null=True
    )
    expenses_included = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_acctg_legal_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_adv_lic_permit_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_electric_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_extermination_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_gas_oil_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_insurance_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_janitor_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_lawn_maintenance_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_maintand_repair_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_management_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_miscellaneous_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_pool_service_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_property_tax_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_replace_reserve_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_retax_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_supplies_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_trash_yn = models.CharField(
        max_length=200,
        null=True
    )
    exp_incl_water_sewer_yn = models.CharField(
        max_length=200,
        null=True
    )
    expiration_date = models.CharField(
        max_length=200,
        null=True
    )
    exterior_features = models.CharField(
        max_length=200,
        null=True
    )
    fee_description = models.CharField(
        max_length=200,
        null=True
    )
    fill_description = models.CharField(
        max_length=200,
        null=True
    )
    fire_protection = models.CharField(
        max_length=200,
        null=True
    )
    fixture_value = models.CharField(
        max_length=200,
        null=True
    )
    floor_description = models.CharField(
        max_length=200,
        null=True
    )
    folio_num2nd_parcel = models.CharField(
        max_length=200,
        null=True
    )
    folio_num3rd_parcel = models.CharField(
        max_length=200,
        null=True
    )
    for_lease_yn = models.CharField(
        max_length=200,
        null=True
    )
    for_sale_yn = models.CharField(
        max_length=200,
        null=True
    )
    front_exposure = models.CharField(
        max_length=200,
        null=True
    )
    furn_annual_rent = models.CharField(
        max_length=200,
        null=True
    )
    furnished_info_list = models.CharField(
        max_length=200,
        null=True
    )
    furnished_info_sold = models.CharField(
        max_length=200,
        null=True
    )
    furn_off_season_rent = models.CharField(
        max_length=200,
        null=True
    )
    furn_seasonal_rent = models.CharField(
        max_length=200,
        null=True
    )
    garage_description = models.CharField(
        max_length=200,
        null=True
    )
    gas_description = models.CharField(
        max_length=200,
        null=True
    )
    geocode_source = models.CharField(
        max_length=200,
        null=True
    )
    geographic_area = models.CharField(
        max_length=200,
        null=True
    )
    gross_operating_income = models.CharField(
        max_length=200,
        null=True
    )
    gross_rent = models.CharField(
        max_length=200,
        null=True
    )
    gross_rent_income = models.CharField(
        max_length=200,
        null=True
    )
    gross_sales = models.CharField(
        max_length=200,
        null=True
    )
    gross_scheduled_income = models.CharField(
        max_length=200,
        null=True
    )
    ground_cover = models.CharField(
        max_length=200,
        null=True
    )
    ground_cover_description = models.CharField(
        max_length=200,
        null=True
    )
    guest_house_description = models.CharField(
        max_length=200,
        null=True
    )
    heating_description = models.CharField(
        max_length=200,
        null=True
    )
    hours_open = models.CharField(
        max_length=200,
        null=True
    )
    housing_older_persons_act = models.CharField(
        max_length=200,
        null=True
    )
    i_dx_opt_in_yn = models.CharField(
        max_length=200,
        null=True
    )
    improvement_height_bus = models.CharField(
        max_length=200,
        null=True
    )
    improvement_height_com = models.CharField(
        max_length=200,
        null=True
    )
    inc_exp_statement_period = models.CharField(
        max_length=200,
        null=True
    )
    information_available = models.CharField(
        max_length=200,
        null=True
    )
    input_broker_remarks = models.CharField(
        max_length=200,
        null=True
    )
    insurance_expense = models.CharField(
        max_length=200,
        null=True
    )
    intended_use = models.CharField(
        max_length=200,
        null=True
    )
    interior_ceiling_height = models.CharField(
        max_length=200,
        null=True
    )
    interior_features = models.CharField(
        max_length=200,
        null=True
    )
    internet_remarks = models.CharField(
        max_length=200,
        null=True
    )
    internet_yn = models.CharField(
        max_length=200,
        null=True
    )
    inventory_value = models.CharField(
        max_length=200,
        null=True
    )
    is_deleted = models.CharField(
        max_length=200,
        null=True
    )
    joint_agency_yn = models.CharField(
        max_length=200,
        null=True
    )
    jurisdiction = models.CharField(
        max_length=200,
        null=True
    )
    land_improvements = models.CharField(
        max_length=200,
        null=True
    )
    land_lease_amount = models.CharField(
        max_length=200,
        null=True
    )
    land_lease_fee_paid_per = models.CharField(
        max_length=200,
        null=True
    )
    last_change_timestamp = models.CharField(
        max_length=200,
        null=True
    )
    last_change_type = models.CharField(
        max_length=200,
        null=True
    )
    last_list_price = models.CharField(
        max_length=200,
        null=True
    )
    last_status = models.CharField(
        max_length=200,
        null=True
    )
    lease_expiration_date = models.CharField(
        max_length=200,
        null=True
    )
    lease_price = models.CharField(
        max_length=200,
        null=True
    )
    lease_term_info = models.CharField(
        max_length=200,
        null=True
    )
    lease_term_remaining = models.CharField(
        max_length=200,
        null=True
    )
    legal_description = models.CharField(
        max_length=200,
        null=True
    )
    lender_approval = models.CharField(
        max_length=200,
        null=True
    )
    licenses = models.CharField(
        max_length=200,
        null=True
    )
    list_agent_mui = models.CharField(
        max_length=200,
        null=True
    )
    list_agent_direct_work_phone = models.CharField(
        max_length=200,
        null=True
    )
    list_agent_email = models.CharField(
        max_length=200,
        null=True
    )
    list_agent_full_name = models.CharField(
        max_length=200,
        null=True
    )
    list_agent_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    listing_contract_date = models.CharField(
        max_length=200,
        null=True
    )
    listing_type = models.CharField(
        max_length=200,
        null=True
    )
    list_office_mui = models.CharField(
        max_length=200,
        null=True
    )
    list_office_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    list_office_name = models.CharField(
        max_length=200,
        null=True
    )
    list_office_phone = models.CharField(
        max_length=200,
        null=True
    )
    list_price = models.CharField(
        max_length=200,
        null=True
    )
    location = models.CharField(
        max_length=200,
        null=True
    )
    locationof_property = models.CharField(
        max_length=200,
        null=True
    )
    lot_depth = models.CharField(
        max_length=200,
        null=True
    )
    lot_description = models.CharField(
        max_length=200,
        null=True
    )
    lot_frontage = models.CharField(
        max_length=200,
        null=True
    )
    lotor_track_num = models.CharField(
        max_length=200,
        null=True
    )
    lot_sq_footage = models.CharField(
        max_length=200,
        null=True
    )
    low_list_price = models.CharField(
        max_length=200,
        null=True
    )
    main_living_area = models.CharField(
        max_length=200,
        null=True
    )
    maintand_repairs_expense = models.CharField(
        max_length=200,
        null=True
    )
    maintenance_charge_month = models.CharField(
        max_length=200,
        null=True
    )
    maintenance_fee_includes = models.CharField(
        max_length=200,
        null=True
    )
    maintenance_includes = models.CharField(
        max_length=200,
        null=True
    )
    maint_fee_paid_per = models.CharField(
        max_length=200,
        null=True
    )
    management_expense = models.CharField(
        max_length=200,
        null=True
    )
    manufactured_home_miscell = models.CharField(
        max_length=200,
        null=True
    )
    manufactured_home_size = models.CharField(
        max_length=200,
        null=True
    )
    map_coordinates = models.CharField(
        max_length=200,
        null=True
    )
    master_bathroom_description = models.CharField(
        max_length=200,
        null=True
    )
    matrix_unique_id = models.CharField(
        max_length=200,
        null=True
    )
    matrix_modified_dt = models.CharField(
        max_length=200,
        null=True
    )
    matrix_testing = models.CharField(
        max_length=200,
        null=True
    )
    maximum_ceiling_height = models.CharField(
        max_length=200,
        null=True
    )
    maximum_leasable_sqft = models.CharField(
        max_length=200,
        null=True
    )
    member_fee_paid_per = models.CharField(
        max_length=200,
        null=True
    )
    membership_purchase_fee = models.CharField(
        max_length=200,
        null=True
    )
    membership_purch_rqd_yn = models.CharField(
        max_length=200,
        null=True
    )
    middle_school = models.CharField(
        max_length=200,
        null=True
    )
    milesto_beach = models.CharField(
        max_length=200,
        null=True
    )
    milesto_expressway = models.CharField(
        max_length=200,
        null=True
    )
    minimum_lease_period = models.CharField(
        max_length=200,
        null=True
    )
    minimum_numof_daysfor_lease = models.CharField(
        max_length=200,
        null=True
    )
    min_sf_living_area_reqmt = models.CharField(
        max_length=200,
        null=True
    )
    miscellaneous = models.CharField(
        max_length=200,
        null=True
    )
    miscellaneous_expense = models.CharField(
        max_length=200,
        null=True
    )
    miscellaneous_improvements = models.CharField(
        max_length=200,
        null=True
    )
    miscellaneous_information = models.CharField(
        max_length=200,
        null=True
    )
    m_ls = models.CharField(
        max_length=200,
        null=True
    )
    m_ls_number = models.CharField(
        max_length=200,
        null=True
    )
    model_name = models.CharField(
        max_length=200,
        null=True
    )
    move_in_dollars = models.CharField(
        max_length=200,
        null=True
    )
    municipal_code = models.CharField(
        max_length=200,
        null=True
    )
    neighborhoods = models.CharField(
        max_length=200,
        null=True
    )
    net_operating_income = models.CharField(
        max_length=200,
        null=True
    )
    num_bays = models.CharField(
        max_length=200,
        null=True
    )
    num_buildings = models.CharField(
        max_length=200,
        null=True
    )
    num_carport_spaces = models.CharField(
        max_length=200,
        null=True
    )
    num_ceiling_fans = models.CharField(
        max_length=200,
        null=True
    )
    num_employees = models.CharField(
        max_length=200,
        null=True
    )
    num_floors = models.CharField(
        max_length=200,
        null=True
    )
    num_garage_spaces = models.CharField(
        max_length=200,
        null=True
    )
    num_interior_levels = models.CharField(
        max_length=200,
        null=True
    )
    num_leases_year = models.CharField(
        max_length=200,
        null=True
    )
    num_loading_doors = models.CharField(
        max_length=200,
        null=True
    )
    num_meters = models.CharField(
        max_length=200,
        null=True
    )
    num_offices = models.CharField(
        max_length=200,
        null=True
    )
    num_parcels = models.CharField(
        max_length=200,
        null=True
    )
    num_parking_spaces = models.CharField(
        max_length=200,
        null=True
    )
    num_seats = models.CharField(
        max_length=200,
        null=True
    )
    num_stories = models.CharField(
        max_length=200,
        null=True
    )
    num_tenants = models.CharField(
        max_length=200,
        null=True
    )
    num_times_leased_year = models.CharField(
        max_length=200,
        null=True
    )
    num_toilets = models.CharField(
        max_length=200,
        null=True
    )
    num_units = models.CharField(
        max_length=200,
        null=True
    )
    occupancy_information = models.CharField(
        max_length=200,
        null=True
    )
    occupancy_percentage = models.CharField(
        max_length=200,
        null=True
    )
    office_fax_number = models.CharField(
        max_length=200,
        null=True
    )
    off_market_date = models.CharField(
        max_length=200,
        null=True
    )
    o_kto_advertise_yn = models.CharField(
        max_length=200,
        null=True
    )
    on_site_utilities = models.CharField(
        max_length=200,
        null=True
    )
    open_house_count = models.CharField(
        max_length=200,
        null=True
    )
    original_entry_timestamp = models.CharField(
        max_length=200,
        null=True
    )
    original_list_price = models.CharField(
        max_length=200,
        null=True
    )
    other_expenses = models.CharField(
        max_length=200,
        null=True
    )
    other_income_expense = models.CharField(
        max_length=200,
        null=True
    )
    owner_agent_yn = models.CharField(
        max_length=200,
        null=True
    )
    ownership = models.CharField(
        max_length=200,
        null=True
    )
    owners_name = models.CharField(
        max_length=200,
        null=True
    )
    owners_phone = models.CharField(
        max_length=200,
        null=True
    )
    p_aceyn = models.CharField(
        max_length=200,
        null=True
    )
    parcel_number = models.CharField(
        max_length=200,
        null=True
    )
    parcel_number_mlx = models.CharField(
        max_length=200,
        null=True
    )
    parking_description = models.CharField(
        max_length=200,
        null=True
    )
    parking_restrictions = models.CharField(
        max_length=200,
        null=True
    )
    parking_space_number = models.CharField(
        max_length=200,
        null=True
    )
    patio_balcony_dimensions = models.CharField(
        max_length=200,
        null=True
    )
    pending_date = models.CharField(
        max_length=200,
        null=True
    )
    pet_restrictions = models.CharField(
        max_length=200,
        null=True
    )
    pets_allowed_yn = models.CharField(
        max_length=200,
        null=True
    )
    photo_count = models.CharField(
        max_length=200,
        null=True
    )
    photo_instructions = models.CharField(
        max_length=200,
        null=True
    )
    photo_modification_timestamp = models.CharField(
        max_length=200,
        null=True
    )
    pool_description = models.CharField(
        max_length=200,
        null=True
    )
    pool_dimensions = models.CharField(
        max_length=200,
        null=True
    )
    pool_yn = models.CharField(
        max_length=200,
        null=True
    )
    possession_information = models.CharField(
        max_length=200,
        null=True
    )
    postal_code = models.CharField(
        max_length=200,
        null=True
    )
    postal_code_plus4 = models.CharField(
        max_length=200,
        null=True
    )
    previous_expiration = models.CharField(
        max_length=200,
        null=True
    )
    previous_status = models.CharField(
        max_length=200,
        null=True
    )
    price_acre = models.CharField(
        max_length=200,
        null=True
    )
    price_change_timestamp = models.CharField(
        max_length=200,
        null=True
    )
    price_front_foot = models.CharField(
        max_length=200,
        null=True
    )
    price_sq_ft = models.CharField(
        max_length=200,
        null=True
    )
    price_unit = models.CharField(
        max_length=200,
        null=True
    )
    property_description = models.CharField(
        max_length=200,
        null=True
    )
    property_detached_yn = models.CharField(
        max_length=200,
        null=True
    )
    property_sq_ft = models.CharField(
        max_length=200,
        null=True
    )
    property_sub_type = models.CharField(
        max_length=200,
        null=True
    )
    property_type = models.CharField(
        max_length=200,
        null=True
    )
    property_type_information = models.CharField(
        max_length=200,
        null=True
    )
    prop_type_typeof_building = models.CharField(
        max_length=200,
        null=True
    )
    provider_key = models.CharField(
        max_length=200,
        null=True
    )
    rail_description = models.CharField(
        max_length=200,
        null=True
    )
    range_price = models.CharField(
        max_length=200,
        null=True
    )
    r_atio_close_price_by_list_price = models.CharField(
        max_length=200,
        null=True
    )
    r_atio_close_price_by_original_list_price = models.CharField(
        max_length=200,
        null=True
    )
    r_atio_current_price_by_sqft = models.CharField(
        max_length=200,
        null=True
    )
    ready_to_activate_yn = models.CharField(
        max_length=200,
        null=True
    )
    real_estate_taxes = models.CharField(
        max_length=200,
        null=True
    )
    rec_lease_mo_fee_paid_per = models.CharField(
        max_length=200,
        null=True
    )
    rec_lease_month = models.CharField(
        max_length=200,
        null=True
    )
    reimbursable_sq_ft = models.CharField(
        max_length=200,
        null=True
    )
    remarks = models.CharField(
        max_length=800,
        null=True
    )
    renewable_rental_yn = models.CharField(
        max_length=200,
        null=True
    )
    renewal_commission = models.CharField(
        max_length=200,
        null=True
    )
    renewal_options = models.CharField(
        max_length=200,
        null=True
    )
    rental_deposit_includes = models.CharField(
        max_length=200,
        null=True
    )
    rental_payment_includes = models.CharField(
        max_length=200,
        null=True
    )
    rent_includes = models.CharField(
        max_length=200,
        null=True
    )
    rent_period = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_april = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_august = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_december = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_february = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_january = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_july = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_june = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_march = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_may = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_november = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_october = models.CharField(
        max_length=200,
        null=True
    )
    rent_status_september = models.CharField(
        max_length=200,
        null=True
    )
    r_eoyn = models.CharField(
        max_length=200,
        null=True
    )
    restrictions = models.CharField(
        max_length=200,
        null=True
    )
    road_description = models.CharField(
        max_length=200,
        null=True
    )
    road_frntg_description = models.CharField(
        max_length=200,
        null=True
    )
    road_frontage = models.CharField(
        max_length=200,
        null=True
    )
    road_type_description = models.CharField(
        max_length=200,
        null=True
    )
    roof = models.CharField(
        max_length=200,
        null=True
    )
    roof_description = models.CharField(
        max_length=200,
        null=True
    )
    room_count = models.CharField(
        max_length=200,
        null=True
    )
    rooms_description = models.CharField(
        max_length=200,
        null=True
    )
    sale_includes = models.CharField(
        max_length=200,
        null=True
    )
    sale_includes_incl = models.CharField(
        max_length=200,
        null=True
    )
    sale_includes_sale = models.CharField(
        max_length=200,
        null=True
    )
    sale_terms = models.CharField(
        max_length=200,
        null=True
    )
    section = models.CharField(
        max_length=200,
        null=True
    )
    security_information = models.CharField(
        max_length=200,
        null=True
    )
    seller_contributions_amt = models.CharField(
        max_length=200,
        null=True
    )
    seller_contributions_yn = models.CharField(
        max_length=200,
        null=True
    )
    selling_agent_mui = models.CharField(
        max_length=200,
        null=True
    )
    selling_agent_direct_work_phone = models.CharField(
        max_length=200,
        null=True
    )
    selling_agent_email = models.CharField(
        max_length=200,
        null=True
    )
    selling_agent_full_name = models.CharField(
        max_length=200,
        null=True
    )
    selling_agent_license_num = models.CharField(
        max_length=200,
        null=True
    )
    selling_agent_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    selling_agent_public_id = models.CharField(
        max_length=200,
        null=True
    )
    selling_office_mui = models.CharField(
        max_length=200,
        null=True
    )
    selling_office_mlsid = models.CharField(
        max_length=200,
        null=True
    )
    selling_office_name = models.CharField(
        max_length=200,
        null=True
    )
    selling_office_phone = models.CharField(
        max_length=200,
        null=True
    )
    senior_high_school = models.CharField(
        max_length=200,
        null=True
    )
    separate_meter_yn = models.CharField(
        max_length=200,
        null=True
    )
    serial_number = models.CharField(
        max_length=200,
        null=True
    )
    service_expense = models.CharField(
        max_length=200,
        null=True
    )
    sewer_description = models.CharField(
        max_length=200,
        null=True
    )
    short_sale_yn = models.CharField(
        max_length=200,
        null=True
    )
    showing_instructions = models.CharField(
        max_length=200,
        null=True
    )
    showing_suite_email_info_yn = models.CharField(
        max_length=200,
        null=True
    )
    showing_suite_setting_yn = models.CharField(
        max_length=200,
        null=True
    )
    sold_priceper_acre = models.CharField(
        max_length=200,
        null=True
    )
    sold_priceper_sf = models.CharField(
        max_length=200,
        null=True
    )
    sourceof_expenses = models.CharField(
        max_length=200,
        null=True
    )
    s_p_amt_sq_ft = models.CharField(
        max_length=200,
        null=True
    )
    spa_yn = models.CharField(
        max_length=200,
        null=True
    )
    special_information = models.CharField(
        max_length=200,
        null=True
    )
    sprinkler_description = models.CharField(
        max_length=200,
        null=True
    )
    sq_ft_l_aof_guest_house = models.CharField(
        max_length=200,
        null=True
    )
    sq_ft_liv_area = models.CharField(
        max_length=200,
        null=True
    )
    sq_ft_occupied = models.CharField(
        max_length=200,
        null=True
    )
    sq_ft_total = models.CharField(
        max_length=200,
        null=True
    )
    state_or_province = models.CharField(
        max_length=200,
        null=True
    )
    status = models.CharField(
        max_length=200,
        null=True
    )
    status_change_timestamp = models.CharField(
        max_length=200,
        null=True
    )
    status_contractual_search_date = models.CharField(
        max_length=200,
        null=True
    )
    street_dir_prefix = models.CharField(
        max_length=200,
        null=True
    )
    street_dir_suffix = models.CharField(
        max_length=200,
        null=True
    )
    street_name = models.CharField(
        max_length=200,
        null=True
    )
    street_number = models.CharField(
        max_length=200,
        null=True
    )
    street_number_numeric = models.CharField(
        max_length=200,
        null=True
    )
    street_suffix = models.CharField(
        max_length=200,
        null=True
    )
    street_view_param = models.CharField(
        max_length=200,
        null=True
    )
    style = models.CharField(
        max_length=200,
        null=True
    )
    styleof_business = models.CharField(
        max_length=200,
        null=True
    )
    styleof_property = models.CharField(
        max_length=200,
        null=True
    )
    style_tran = models.CharField(
        max_length=200,
        null=True
    )
    sub_board_id = models.CharField(
        max_length=200,
        null=True
    )
    subdivision_complex_bldg = models.CharField(
        max_length=200,
        null=True
    )
    subdivision_information = models.CharField(
        max_length=200,
        null=True
    )
    subdivision_name = models.CharField(
        max_length=200,
        null=True
    )
    subdivision_number = models.CharField(
        max_length=200,
        null=True
    )
    supplement_count = models.CharField(
        max_length=200,
        null=True
    )
    supplement_modification_timestamp = models.CharField(
        max_length=200,
        null=True
    )
    supply_expense = models.CharField(
        max_length=200,
        null=True
    )
    surface_description = models.CharField(
        max_length=200,
        null=True
    )
    tax_amount = models.CharField(
        max_length=200,
        null=True
    )
    tax_information = models.CharField(
        max_length=200,
        null=True
    )
    tax_year = models.CharField(
        max_length=200,
        null=True
    )
    temp_off_market_date = models.CharField(
        max_length=200,
        null=True
    )
    tenant_pays = models.CharField(
        max_length=200,
        null=True
    )
    terms_available = models.CharField(
        max_length=200,
        null=True
    )
    terms_considered = models.CharField(
        max_length=200,
        null=True
    )
    total_assumable_loans = models.CharField(
        max_length=200,
        null=True
    )
    total_expenses = models.CharField(
        max_length=200,
        null=True
    )
    total_floors_in_building = models.CharField(
        max_length=200,
        null=True
    )
    total_move_in_dollars = models.CharField(
        max_length=200,
        null=True
    )
    total_numof_units_in_buildin = models.CharField(
        max_length=200,
        null=True
    )
    total_numof_units_in_complex = models.CharField(
        max_length=200,
        null=True
    )
    township_range = models.CharField(
        max_length=200,
        null=True
    )
    training_available_yn = models.CharField(
        max_length=200,
        null=True
    )
    transaction_type = models.CharField(
        max_length=200,
        null=True
    )
    transaction_type_mlx = models.CharField(
        max_length=200,
        null=True
    )
    trash_expense = models.CharField(
        max_length=200,
        null=True
    )
    typeof_association = models.CharField(
        max_length=200,
        null=True
    )
    typeof_building = models.CharField(
        max_length=200,
        null=True
    )
    typeof_business = models.CharField(
        max_length=200,
        null=True
    )
    typeof_contingencies = models.CharField(
        max_length=200,
        null=True
    )
    typeof_governing_bodies = models.CharField(
        max_length=200,
        null=True
    )
    typeof_ownership = models.CharField(
        max_length=200,
        null=True
    )
    typeof_property = models.CharField(
        max_length=200,
        null=True
    )
    typeof_soil = models.CharField(
        max_length=200,
        null=True
    )
    typeof_trees = models.CharField(
        max_length=200,
        null=True
    )
    unfurn_annual_rent = models.CharField(
        max_length=200,
        null=True
    )
    unfurn_off_season_rent = models.CharField(
        max_length=200,
        null=True
    )
    unfurn_seasonal_rent = models.CharField(
        max_length=200,
        null=True
    )
    unit_count = models.CharField(
        max_length=200,
        null=True
    )
    unit_design = models.CharField(
        max_length=200,
        null=True
    )
    unit_floor_location = models.CharField(
        max_length=200,
        null=True
    )
    unit_number = models.CharField(
        max_length=200,
        null=True
    )
    unit_view = models.CharField(
        max_length=200,
        null=True
    )
    usage = models.CharField(
        max_length=200,
        null=True
    )
    usage_description = models.CharField(
        max_length=200,
        null=True
    )
    utilities_available = models.CharField(
        max_length=200,
        null=True
    )
    utility_expense = models.CharField(
        max_length=200,
        null=True
    )
    utility_room_dimension = models.CharField(
        max_length=200,
        null=True
    )
    vacancy_rate = models.CharField(
        max_length=200,
        null=True
    )
    var_dual_rate_comp_yn = models.CharField(
        max_length=200,
        null=True
    )
    view = models.CharField(
        max_length=200,
        null=True
    )
    virtual_tour = models.CharField(
        max_length=200,
        null=True
    )
    water_access = models.CharField(
        max_length=200,
        null=True
    )
    water_description = models.CharField(
        max_length=200,
        null=True
    )
    waterfront_description = models.CharField(
        max_length=200,
        null=True
    )
    waterfront_frontage = models.CharField(
        max_length=200,
        null=True
    )
    waterfront_property_yn = models.CharField(
        max_length=200,
        null=True
    )
    water_view = models.CharField(
        max_length=200,
        null=True
    )
    waterview_description = models.CharField(
        max_length=200,
        null=True
    )
    web_address = models.CharField(
        max_length=200,
        null=True
    )
    windows_treatment = models.CharField(
        max_length=200,
        null=True
    )
    withdrawn_date = models.CharField(
        max_length=200,
        null=True
    )
    year_built_description = models.CharField(
        max_length=200,
        null=True
    )
    year_established = models.CharField(
        max_length=200,
        null=True
    )
    yearof_addition = models.CharField(
        max_length=200,
        null=True
    )



class PropertyViewCount(models.Model):
    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE
    )
    mon_count = models.IntegerField(
        default = 0
    )
    mon_date = models.DateTimeField(
        default = timezone.now
    )
    tues_count = models.IntegerField(
        default = 0
    )
    tues_date = models.DateTimeField(
        default = timezone.now
    )
    wed_count = models.IntegerField(
        default = 0
    )
    wed_date = models.DateTimeField(
        default = timezone.now
    )
    thurs_count = models.IntegerField(
        default = 0
    )
    thurs_date = models.DateTimeField(
        default = timezone.now
    )
    fri_count = models.IntegerField(
        default = 0
    )
    fri_date = models.DateTimeField(
        default = timezone.now
    )
    sat_count = models.IntegerField(
        default = 0
    )
    sat_date = models.DateTimeField(
        default = timezone.now
    )
    sun_count = models.IntegerField(
        default = 0
    )
    sun_date = models.DateTimeField(
        default = timezone.now
    )
    weekly_count = models.IntegerField(
        default = 0
    )
    total_count = models.IntegerField(
        default = 0
    )



class Rooms(models.Model):
    input_entry_order = models.IntegerField(
        null=True
    )
    is_deleted = models.NullBooleanField(
        null=True
    )
    listing_mui = models.BigIntegerField(
        null=True
    )
    matrix_unique_id = models.BigIntegerField(
        null=True,
        unique=True
    )
    matrix_modified_dt = models.DateTimeField(
        null=True
    )
    room_dimension = models.CharField(
        max_length=200,
        null=True
    )
    room_type = models.CharField(
        max_length=200,
        null=True
    )



class Units(models.Model):
    ARent = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True
    )
    b_rent = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True
    )
    efficiency_yn = models.NullBooleanField(
        null=True
    )
    equipment = models.CharField(
        max_length=200,
        null=True
    )
    furnished_yn = models.NullBooleanField(
        null=True
    )
    furniture_info = models.CharField(
        max_length=200,
        null=True
    )
    hotel_room_yn = models.NullBooleanField(
        null=True
    )
    input_entry_order = models.IntegerField(
        null=True
    )
    is_deleted = models.NullBooleanField(
        null=True
    )
    lease_ends_info = models.CharField(
        max_length=200,
        null=True
    )
    listing_mui = models.BigIntegerField(
        null=True
    )
    matrix_unique_id = models.BigIntegerField(
        null=True,
        unique=True
    )
    MatrixModifiedDT = models.DateTimeField(
        null=True
    )
    monthly_income = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True
    )
    numof_baths = models.CharField(
        max_length=200,
        null=True
    )
    numof_beds = models.IntegerField(
        null=True
    )
    numof_f_baths = models.IntegerField(
        null=True
    )
    numof_h_baths = models.IntegerField(
        null=True
    )
    numof_units = models.IntegerField(
        null=True
    )
    parking = models.CharField(
        max_length=200,
        null=True
    )
    rental_period_a = models.CharField(
        max_length=200,
        null=True
    )
    rental_period_b = models.CharField(
        max_length=200,
        null=True
    )
    room_description = models.CharField(
        max_length=200,
        null=True
    )
    sq_ft = models.IntegerField(
        null=True
    )
    unit_number = models.IntegerField(
        null=True
    )
    unit_type = models.CharField(
        max_length=200,
        null=True
    )


class PropertyMedia(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    path = models.CharField(
        max_length=200,
        unique=True
    )
    content_type = models.CharField(
        max_length=200
    )
    description = models.CharField(
        max_length=200
    )


class PropertyLocation(models.Model):
    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE
    )
    point = gis_models.PointField()
    level = models.CharField(
        max_length=60
    )


class List(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    properties = models.ManyToManyField(
        'property',
        blank=True
    )

class Tag(models.Model):
    uid = models.ForeignKey('user.User')
    pid = models.ForeignKey(Property)
    tag = models.CharField(
        max_length=100
    )
    class Meta:
        unique_together = ["uid", "pid", "tag"]

class Theme(models.Model):
    theme_name = models.CharField(
        max_length=200,
        null=True
    )
    color_1 = models.CharField(
        max_length=7,
        null=True
    )
    color_2 = models.CharField(
        max_length=7,
        null=True
    )
    color_3 = models.CharField(
        max_length=7,
        null=True
    )
    color_4 = models.CharField(
        max_length=7,
        null=True
    )
    color_5 = models.CharField(
        max_length=7,
        null=True
    )
    color_6 = models.CharField(
        max_length=7,
        null=True
    )
    image = models.CharField(
        max_length=50,
        null=True
    )

class SavedSearch(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    query_string = models.CharField(
        max_length=1023,
        null=True,
        blank=True
    )

class BHGeometry(models.Model):
    query_string = models.CharField(
        max_length=1023,
        null=True,
        blank=True
    )

class SearchHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    time_created = models.DateTimeField(
        auto_now_add=True
    )
    count = models.IntegerField(
        default=0
    )
    query_string = models.CharField(
        max_length=1023,
        null=True,
        blank=True,
        unique=True
    )
