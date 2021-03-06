from pytest import mark

from tests.test_data_const import EXISTED_PET_ID, NOT_EXISTED_PET_ID
from utils.api import get_pet
from utils.const_error import INV_RESP_CODE
from utils.data_utils import is_json_valid_by_scheme


@mark.positive
@mark.parametrize("pet_id", [EXISTED_PET_ID])
def test_get_pet_positive(pet_id):
    response = get_pet(pet_id)

    assert response.status_code == 200, INV_RESP_CODE
    assert is_json_valid_by_scheme(response.text, "get_pet")


@mark.negative
@mark.parametrize("pet_id", [NOT_EXISTED_PET_ID])
def test_get_pet_negative(pet_id):
    response = get_pet(pet_id)

    assert response.status_code == 404, INV_RESP_CODE
    assert is_json_valid_by_scheme(response.text, "get_pet_error")
