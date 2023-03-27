from http import HTTPStatus

from flasgger import swag_from
from flask import request, wrappers

from src import (DriverAdaptor, app, data_to_json, data_to_xml,
                 make_json_response, make_xml_response)


@app.route('/report', methods=['GET'])
@swag_from('swagger/report.yml')
def show_report() -> wrappers.Response:
    instance = DriverAdaptor()
    sorted_data = instance.sort_data(request.args.get('order') == "desc")
    if request.args.get('format') == "json":
        return make_json_response([x.__dict__ for x in sorted_data], HTTPStatus.OK)
    elif request.args.get('format') == "xml":
        return make_xml_response(data_to_xml(sorted_data), HTTPStatus.OK)


@app.route('/report/drivers', methods=['GET'])
@swag_from('swagger/drivers.yml')
def show_drivers() -> wrappers.Response:
    instance = DriverAdaptor()
    sorted_data = instance.sort_data(request.args.get('order') == "desc")
    if request.args.get('format') == "json":
        return make_json_response(data_to_json(sorted_data), HTTPStatus.OK)
    elif request.args.get('format') == "xml":
        return make_xml_response(data_to_json(sorted_data), HTTPStatus.OK)


@app.route('/report/drivers/<driver_code>', methods=['GET'])
@swag_from('swagger/driver.yml')
def get_info(driver_code: str) -> wrappers.Response:
    instance = DriverAdaptor()
    driver = instance.get_driver("abbreviation", driver_code)
    if driver is None:
        return make_json_response({"message": "No such driver"}, HTTPStatus.NOT_FOUND)
    if request.args.get('format') == "json":
        return make_json_response(driver.__dict__, HTTPStatus.OK)
    elif request.args.get('format') == "xml":
        return make_xml_response(driver.__dict__, HTTPStatus.OK)


@app.errorhandler(404)
def handle_exception(e) -> wrappers.Response:
    return make_json_response({"message": "Page Not Found"}, HTTPStatus.NOT_FOUND)
