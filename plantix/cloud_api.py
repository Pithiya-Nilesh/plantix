from google.cloud import vision
from google.cloud.vision_v1 import types
from google.oauth2 import service_account
from google.cloud import vision_v1
from google.protobuf.json_format import MessageToJson
import io
import frappe
from frappe import _

def detect_labels(file_content, mobile_number, image_url):
    # Define your service account key directly in your code
    service_account_info = {
        "type": "service_account",
        "project_id": "farmer-doctor",
        "private_key_id": "d7a7baa81ac1b8b4f77d4db61971ef447ae7519e",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDQcvG8DecQHb7Z\nLWjkhK3ogJR8dl+rgRdEZxblJtoSg18I1OwajiDDnq6rX5BJ0NC8pWn9oM4/8Y15\ntLzaeM/6Aqc9qFJIOt8Sjlsfs6JH+RDR+gFv48/eFOLoVKzZCfBGiUIxjbx389y0\nG3XkkJYOSWqyS7ECHC2Ue9bHDs+O3IZmu7ZvPpTHZPbc9P5imeYv8SlfC+a1+6DF\nPEGmCZsvmd5in5v2jm9gwEw2vpVuoVzFDjI0rXI7ky7J5B2AHGlIS6jMSHp+iMV2\nGqgNbRMRScSczO/QjCCfJRMGsTA6aV44sRKe81sQvUuTmmnwFh2blLNBJ9o4p1w/\n8yGWskD3AgMBAAECggEAGp7LS1JVM2QxFsgrUJ+3G+2ryNdPMXZbc9Ncg6g6Cko3\nrUeP3XZQLdtKgD1EjoC535WaWxcZr+XXxPa1dYsfOFT1abTgyTOngFWownws2dcv\ndDlizJjB16FANx51MoSH6GIoD28D5ifBBElLfYSPfUSX+Swcb2IM2h0UmThFfn9l\nNAaTs8iDgZ7WOd9dDnTC57g5dH4VMCgB3eF9tVzwjs+lrFvUQHNJJ3aLn38qq2I/\nswffFqtINVMEr6Jouwgfy9FKLdLUdoGrgfWjOkwyLY1LaPawlVzBYUCoJeD0KNQZ\nYN6Gy8y2Vy78yPdEAL1tPwOGMh8X04CMDPuX6XNkxQKBgQDnHkjXgCQElmMqAJr7\nz/qV3rriOa4UEU/r41RohNE9om92BZuaQbaFbLJQnEbabPQiSy5gZe0P1cGL/RXw\nqo2ljpnKoy4EMOLGlrejP+H3GLG8ntoQDtV2UcFZLInUV6SmEOnw6N54ukVdoO2W\nvuN94eSyq55LAh/Gt95jHBzLDQKBgQDm4+JyN0SM+cVw5M5ljwDYbluS35SdRsb1\niDKV24mzCP3rQuTheWVchovQ7tGHkpIr5Iel7dEaowRdVOptNPa4eJZS+EVCnakd\ndLWVVGO+hPmTO4h5kCbd/ph99hOo2ZmCL2WhODMRyCLOXjfkD5WiogkJDWZivHme\nkbYr50QrEwKBgQDLr3cG5ZnYqSlP9SSh1JPFzXvqsGborLFA9SKI0rUNmsCcxShz\ndIKFaFxmirQvAGLQbm2661lX4U0oMK5LYiRfyiNj4RhG/UZ/OokxSLW+7XaHA4Cv\nMkOSeU7rZkM6bttet/1VIgYfZBqJ/7AkcKtRX+oMRQ/Gj2Kt4ZIOytHdaQKBgQDO\n7SdyM4QVUHiaIAW2UT5xuh4J+KTpe5guTxz+311+fi2LXk1gofqsvMyruI1CkqK8\nAblshUGlPLpZpxPeQdxoIXKf82+nL0N0abefmJ04D1bZlD5QrFeZF2a1ZQfjiPki\nCrZrkcF7S0GecCRpGWqC8fNlEIRVMxNQgMiiekbGzwKBgQCd9DRQH/MryDAzrAQv\nJ/2W6HgdbWWom3XE4kl1pkhfZrLJvYiwu3X6OHW3qWagLWDUVZZb5J62n/IILnXq\nxDZXzR8a4nJt9+Wq08Xdb4/mu+yfSN0z+rU1b467u/ULbUSl5tPSnla6pVpS+NHm\nUKwS2lpfsCaYbwWTUU1XWG4mmg==\n-----END PRIVATE KEY-----\n",
        "client_email": "farmer-doctor@farmer-doctor.iam.gserviceaccount.com",
        "client_id": "110758421598125079924",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/farmer-doctor%40farmer-doctor.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }


    # Create credentials from the defined service account info
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info,
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

    sr = frappe.new_doc("Scan Report")
    sr.mobile_no = mobile_number
    sr.image = image_url
    if m_data:
        sr.found_result = 1
        sr.result = m_data[0]
        sr.google_result = str(data)
        sr.insert(ignore_permissions=True)
        frappe.db.commit()
        # return {"details": frappe.get_doc("Diseases Response And Products", m_data[0]), "g_data":data}
        return frappe.get_doc("Diseases Response And Products", m_data[0])
        # return data
    
    else:
        sr.found_result = 0
        sr.google_result = str(data)
        sr.insert(ignore_permissions=True)
        frappe.db.commit()
    
    # return frappe.get_doc("Diseases Response And Products", "1b7cc6007c")


@frappe.whitelist()
def check_image(image_url):
    return detect_labels(image_url)


@frappe.whitelist(allow_guest=True)
def scan_image(mobile_number):
    # if frappe.session.user == "Guest":
    #     frappe.throw(_("You need to be logged in to upload an image")
    
    count = frappe.db.count('Scan Report', {'mobile_no': mobile_number})
    if mobile_number == 1234567890:
        count = 0

    if count >= 3:
        return "Reach Limit"

    else:
        # if frappe.request.method != "POST":
        #     frappe.throw(_("Invalid Request"))

        import os
        from frappe.utils.file_manager import save_file, save_file_on_filesystem
        from frappe import get_site_path

        uploaded_file = frappe.request.files.get("image")
        print("\n\n mobile number", mobile_number)

        if not uploaded_file:
            frappe.throw(_("No image file attached"))

        # Ensure the file content is of type bytes
        file_content = uploaded_file.read()

        # Assuming uploaded_file is the FileStorage object from your file upload
        file_name = uploaded_file.filename + frappe.utils.random_string(5)

        # Save the file
        file_doc = save_file_on_filesystem(file_name, file_content)

        # Access the file URL
        image_url = file_doc.get('file_url')

        return detect_labels(file_content, mobile_number, image_url)