# body_temp = """{
#  "upgrade": {
#   "package-name": "$PACKAGE_NAME",
#   "device-name": "$DEVICE_NAME",
#   "upgrade-type": "deb-package-upgrade"
#  }
# }"""

body_temp = """{
 "input": {
  "package-name": "$PACKAGE_NAME",
  "device-name": "$DEVICE_NAME",
  "upload-only": "$UPLOAD_ONLY"
 }
}"""

