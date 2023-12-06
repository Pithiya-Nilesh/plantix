from google.cloud import vision
from google.cloud.vision_v1 import types
from google.oauth2 import service_account
from google.cloud import vision_v1
from google.protobuf.json_format import MessageToJson
import io
import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def scan_image(mobile_number):
    # if frappe.session.user == "Guest":
    #     frappe.throw(_("You need to be logged in to upload an image")

    count = frappe.db.count('Scan Report', {'mobile_no': mobile_number})
    if mobile_number == '1234567890':
        count = 0

    if count >= 3:
        return "Reach Limit"

    else:
        # if frappe.request.method != "POST":
        #     frappe.throw(_("Invalid Request"))

         return frappe.get_doc("Diseases Response And Products", "b585d4573c")