from google.cloud import vision
from google.cloud.vision_v1 import types
from google.oauth2 import service_account
from google.cloud import vision_v1
from google.protobuf.json_format import MessageToJson
import io
import frappe
from frappe import _

def detect_labels(file_content):
    credentials = service_account.Credentials.from_service_account_file(
        # '/home/nilesh-pithiya/Downloads/astro-sanskar-demo-65acfdc58ba9.json',
        '/home/nilesh-pithiya/Downloads/farmer-doctor-d7a7baa81ac1.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    client = vision.ImageAnnotatorClient(credentials=credentials)

    image = types.Image(content=file_content)

    response = client.label_detection(image=image)

    labels = response.label_annotations

    data = []
    for label in labels:
        data.append(label.description)
        # print("\n\n label", label)
    print("\n\n data", data)
    # return data

    # data = ['Food', 'Plant', 'Fruit', 'Terrestrial plant', 'Natural foods', 'Produce', 'Tree', 'Flowering plant', 'Fruit tree', 'Twig']

    f_data = frappe.db.get_list("Diseases Response And Products", fields=["name", "label_found"])
    import json
    import ast
    m_data = []
    for i in f_data:
        if i["label_found"]:
            python_list = ast.literal_eval(i["label_found"])
            final_data = all(element in data for element in python_list)
            if final_data:
                m_data.append(i["name"])

    if m_data: 
        return frappe.get_doc("Diseases Response And Products", m_data[0]), data

@frappe.whitelist()
def check_image(image_url):
    return detect_labels(image_url)

@frappe.whitelist(allow_guest=True)
def scan_image():
    # if frappe.session.user == "Guest":
    #     frappe.throw(_("You need to be logged in to upload an image"))

    if frappe.request.method != "POST":
        frappe.throw(_("Invalid Request"))

    uploaded_file = frappe.request.files.get("image")

    if not uploaded_file:
        frappe.throw(_("No image file attached"))

    # Ensure the file content is of type bytes
    file_content = uploaded_file.read()

    return detect_labels(file_content)
