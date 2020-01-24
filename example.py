import os
import zipfile
import tempfile
import pupilcloud

DOWNLOADS_PATH = "./downloads"
API_KEY = ""

api = pupilcloud.Api(api_key=API_KEY, downloads_path=DOWNLOADS_PATH,)

account = api.get_profile().result
print(f"Pupil Cloud Stats for {account.email}:")
print(80 * "-")
recordings = api.get_recordings().result
templates = api.get_templates().result
wearers = api.get_wearers().result
total_size_gb = sum(r.size for r in recordings) / 1024 / 1024 / 1024
print(f"{len(recordings)} recordings ({round(total_size_gb, 2)} GB)")
print(f"{len(wearers)} wearers")
print(f"{len(templates)} templates")
print(80 * "-")
print(80 * "-")

recordings = sorted(recordings, key=lambda rec: rec.recorded_at or rec.created_at)
recording = recordings[-1]
template = api.get_template(recording.template_id).result
wearer = api.get_wearer(recording.wearer_id).result

print(f"Latest recording: ")
print(80 * "-")
print(f"ID: {recording.id}")
print(f"Recorded: {recording.recorded_at}")
print(f"Size: {recording.size/1024/1024} MB")
print(f"Wearer: {wearer.name} ({wearer.id})")
print(f"Template: {template.name} ({template.id})")
print(f"Template data:")
for template_item in template.items:
    answers = recording.template_data.get(template_item.id)
    print(f"    {template_item.title} ({template_item.input_type}): {answers}")

print(f"File list:")
file_list = api.get_recording_files(recording.id).result
for file in file_list:
    print(f"    {file.name} ({file.size_bytes})")

print(80 * "-")
print(80 * "-")

print(f"Reading info.json in memory...")
info_json_bytes = api.download_recording_file(
    recording_id=recording.id, filename="info.json", _preload_content=False
).read()
print(info_json_bytes)

print(f"Downloading and extracting recording zip...")
zip_file_path = api.download_recording_zip(recording_id=recording.id)
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(DOWNLOADS_PATH)
