from Tests.api_restful_booker_tests.test_booking_read import TestsBooking


class TestBookingUpdate(TestsBooking):
    def test_update_booking(self, booking_payload, booking_client, create_booking_id, auth_cookie_token):
        # booking_payload = {
        #     "firstname": "Updated",
        #     "lastname": "User",
        #     "totalprice": 999,
        #     "depositpaid": True,
        #     "bookingdates": {"checkin": "2026-03-01", "checkout": "2026-03-10"},
        #     "additionalneeds": "Dinner"}

        put_response = booking_client.update_booking(create_booking_id, booking_payload, auth_cookie_token)

        assert put_response.status_code == 200, f"Access forbidden, verify auth cookies"
        put_body = put_response.json()

        assert booking_payload["firstname"] == put_body['firstname'], f"First Name - {booking_payload["firstname"]} was not updated in put_body"
        assert booking_payload["lastname"] == put_body['lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated in put_body"

        get_response = booking_client.get_booking(create_booking_id)
        assert get_response.status_code == 200

        get_body = get_response.json()

        assert booking_payload["firstname"] == get_body['firstname'], f"First Name - {booking_payload["firstname"]} was not updated after put request"
        assert booking_payload["lastname"] == get_body['lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated after put request"

    def test_update_booking_without_token_negative(self, booking_payload, booking_client, create_booking_id):
        # booking_payload = {
        #     "firstname": "Updated",
        #     "lastname": "User",
        #     "totalprice": 999,
        #     "depositpaid": True,
        #     "bookingdates": {"checkin": "2026-03-01", "checkout": "2026-03-10"},
        #     "additionalneeds": "Dinner"}

        put_response = booking_client.update_booking(create_booking_id, booking_payload)
        assert put_response.status_code in (403, 401), f"Access is given without auth cookies"

    def test_patch_booking(self, booking_payload, booking_client, create_booking_id, auth_cookie_token):
        # booking_payload = {
        #     "firstname": "Mikie",
        #     "lastname": "Howard"}
        response = booking_client.patch_booking(create_booking_id, booking_payload, auth_cookie_token)
        assert response.status_code == 200, "Patch request is failed"
        patch_body = response.json()

        assert booking_payload["firstname"] == patch_body['firstname'], f"First Name - {booking_payload["firstname"]} was not updated in patch_body"
        assert booking_payload["lastname"] == patch_body['lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated in patch_body"

        get_response = booking_client.get_booking(create_booking_id)
        get_body = get_response.json()

        assert booking_payload["firstname"] == get_body['firstname'], f"First Name - {booking_payload["firstname"]} was not updated after patch request"
        assert booking_payload["lastname"] == get_body['lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated after patch request"

    def test_patch_booking_without_token_negative(self, booking_client, create_booking_id):
        booking_payload = {
            "firstname": "Jo"}
        patch_response = booking_client.patch_booking(booking_client, create_booking_id, booking_payload)
        assert patch_response.status_code in (403, 401), f"Access is given without auth cookies"

        get_response = booking_client.get_booking(create_booking_id)
        get_body = get_response.json()

        assert booking_payload["firstname"] == get_body["firstname"], f"{booking_payload["firstname"]} was changes without auth token"