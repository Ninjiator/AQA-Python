from Tests.api_restful_booker_tests.test_booking_read import TestsBooking


class TestDeleteBooking(TestsBooking):
    def test_delete_booking(self, booking_client, create_booking_id):
        response = booking_client.delete_booking(create_booking_id)
        assert response.status_code == 201, f"Booking id - {create_booking_id} is not deleted"

        response = booking_client.get_booking(create_booking_id)
        assert response.status_code == 404, f"Booking id - {create_booking_id} still exist"

    def test_delete_booking_without_token_negative(self, booking_client, create_booking_id):
        response = booking_client.delete_booking(create_booking_id, False)
        assert response.status_code == 403, f"Booking id - {create_booking_id} was deleted without auth token"


