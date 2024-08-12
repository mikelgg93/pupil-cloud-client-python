# pupilcloud.CloudClientApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_static_image_mapper_enrichments_recording_fixation**](CloudClientApi.md#clear_static_image_mapper_enrichments_recording_fixation) | **POST** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations:clear | Clear or resets all the mapped fixation of recording&#39;s
[**create_recording_event**](CloudClientApi.md#create_recording_event) | **POST** /workspaces/{workspace_id}/recordings/{recording_id}/scene_camera.{format} | Create recording event
[**create_workspace_invitation**](CloudClientApi.md#create_workspace_invitation) | **POST** /workspaces/{workspace_id}/invites | Create a workspace invitation
[**delete_aoi**](CloudClientApi.md#delete_aoi) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois/{aoi_id} | Delete an aoi
[**delete_aois**](CloudClientApi.md#delete_aois) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois | Delete multiple aois
[**delete_aois_0**](CloudClientApi.md#delete_aois_0) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois:stats | Delete multiple aois
[**delete_filter**](CloudClientApi.md#delete_filter) | **DELETE** /workspaces/{workspace_id}/filters/{filter_id} | Delete a filter
[**delete_filters**](CloudClientApi.md#delete_filters) | **DELETE** /workspaces/{workspace_id}/filters/ | Delete multiple filters
[**delete_label**](CloudClientApi.md#delete_label) | **DELETE** /workspaces/{workspace_id}/labels/{label_id} | Delete a label
[**delete_labels**](CloudClientApi.md#delete_labels) | **DELETE** /workspaces/{workspace_id}/labels/ | Delete multiple labels
[**delete_project_enrichment_resource**](CloudClientApi.md#delete_project_enrichment_resource) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id} | Delete a project enrichment
[**delete_project_recording_event_resource**](CloudClientApi.md#delete_project_recording_event_resource) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events/{event_id} | Delete a project recording event
[**delete_project_resource**](CloudClientApi.md#delete_project_resource) | **DELETE** /workspaces/{workspace_id}/projects/{project_id} | Delete a project
[**delete_projects_resource**](CloudClientApi.md#delete_projects_resource) | **DELETE** /workspaces/{workspace_id}/projects/ | Delete multiple projects
[**delete_recording**](CloudClientApi.md#delete_recording) | **DELETE** /workspaces/{workspace_id}/recordings/{recording_id} | Delete a recording
[**delete_recording_event_resource**](CloudClientApi.md#delete_recording_event_resource) | **DELETE** /workspaces/{workspace_id}/recordings/{recording_id}/events/{event_id} | Delete a recording event
[**delete_recordings**](CloudClientApi.md#delete_recordings) | **DELETE** /workspaces/{workspace_id}/recordings/ | Delete multiple recordings
[**delete_static_image_mapper_enrichments_recording_fixation**](CloudClientApi.md#delete_static_image_mapper_enrichments_recording_fixation) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations/{fixation_id} | Deletes coordinates of a particular fixation of recording&#39;s
[**delete_template**](CloudClientApi.md#delete_template) | **DELETE** /workspaces/{workspace_id}/templates/{template_id} | Delete a template
[**delete_templates**](CloudClientApi.md#delete_templates) | **DELETE** /workspaces/{workspace_id}/templates/ | Delete multiple templates
[**delete_token**](CloudClientApi.md#delete_token) | **DELETE** /auth/tokens/{token_id} | Delete an access token
[**delete_visualization_config**](CloudClientApi.md#delete_visualization_config) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs/{visualization_config_id} | Delete a visualization config
[**delete_wearer**](CloudClientApi.md#delete_wearer) | **DELETE** /workspaces/{workspace_id}/wearers/{wearer_id} | Delete a wearer
[**delete_wearers**](CloudClientApi.md#delete_wearers) | **DELETE** /workspaces/{workspace_id}/wearers/ | Delete multiple wearers
[**delete_workspace**](CloudClientApi.md#delete_workspace) | **DELETE** /workspaces/{workspace_id} | Delete a workspace
[**delete_workspace_invitation**](CloudClientApi.md#delete_workspace_invitation) | **DELETE** /auth/profile/invites/{token} | Delete a workspace invitation
[**delete_workspace_invitation_0**](CloudClientApi.md#delete_workspace_invitation_0) | **DELETE** /workspaces/{workspace_id}/invites/{token} | Delete a workspace invitation
[**delete_workspace_member**](CloudClientApi.md#delete_workspace_member) | **DELETE** /workspaces/{workspace_id}/members/{user_id} | Delete a workspace member from a workspace
[**download_raw_data_export_zip**](CloudClientApi.md#download_raw_data_export_zip) | **GET** /workspaces/{workspace_id}/recordings:raw-data-export | 
[**download_recording_file**](CloudClientApi.md#download_recording_file) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/files/{filename} | Download a recording&#39;s file
[**download_recording_zip**](CloudClientApi.md#download_recording_zip) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}.zip | Download recording files as a zip file
[**download_recordings_zip**](CloudClientApi.md#download_recordings_zip) | **GET** /workspaces/{workspace_id}/recordings.zip | Download multiple recordings in zip archive
[**export_static_image_mapper_enrichment**](CloudClientApi.md#export_static_image_mapper_enrichment) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{static_enrichment_id}/export | Export static image mapper enrichment
[**get_aoi**](CloudClientApi.md#get_aoi) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois/{aoi_id} | Returns an aoi with {aoi_id}
[**get_aoi_stats**](CloudClientApi.md#get_aoi_stats) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois:stats | List all aois of an enrichment
[**get_aois**](CloudClientApi.md#get_aois) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois | List all aois of an enrichment
[**get_apriltag_detections**](CloudClientApi.md#get_apriltag_detections) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/apriltags | Get apritag data for surface enrichment
[**get_apriltags_at_timestamp**](CloudClientApi.md#get_apriltags_at_timestamp) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/apriltags_at_timestamp/ | 
[**get_canny_sso_token**](CloudClientApi.md#get_canny_sso_token) | **GET** /auth/canny-sso | Returns the canny
[**get_download_heatmap**](CloudClientApi.md#get_download_heatmap) | **GET** /workspaces/{workspace_id}/heatmap/zip_download | download zip file with heatmaps
[**get_filter**](CloudClientApi.md#get_filter) | **GET** /workspaces/{workspace_id}/filters/{filter_id} | Returns a filter with {filter_id}
[**get_filters**](CloudClientApi.md#get_filters) | **GET** /workspaces/{workspace_id}/filters/ | List all filters
[**get_hardware**](CloudClientApi.md#get_hardware) | **GET** /hardware/{serial_number}/calibration.{version} | Returns calibration
[**get_heatmap**](CloudClientApi.md#get_heatmap) | **GET** /workspaces/{workspace_id}/heatmap/ | get heatmap image or json data
[**get_heatmap_background**](CloudClientApi.md#get_heatmap_background) | **GET** /workspaces/{workspace_id}/heatmap/background | get heatmap background for overlay
[**get_label**](CloudClientApi.md#get_label) | **GET** /workspaces/{workspace_id}/labels/{label_id} | Returns a label with {label_id}
[**get_labels**](CloudClientApi.md#get_labels) | **GET** /workspaces/{workspace_id}/labels/ | List all labels
[**get_markerless**](CloudClientApi.md#get_markerless) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id} | Get markerless definition
[**get_markerless_camera_poses**](CloudClientApi.md#get_markerless_camera_poses) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/recordings/{recording_id}/camera_pose.{format} | get markerless camera poses
[**get_markerless_detections_timeline**](CloudClientApi.md#get_markerless_detections_timeline) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/recordings/{recording_id}/gaze_in_aoi_timeline | Recording markerless detections
[**get_markerless_gaze_on_aoi**](CloudClientApi.md#get_markerless_gaze_on_aoi) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/gaze_in_aoi | get gaze on aoi data for markerless enrichment
[**get_markerless_point_cloud**](CloudClientApi.md#get_markerless_point_cloud) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/point_cloud.{format} | 
[**get_profile**](CloudClientApi.md#get_profile) | **GET** /auth/profile | Returns the current logged in user based on auth token
[**get_project_enrichment**](CloudClientApi.md#get_project_enrichment) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id} | Get a project enrichment
[**get_project_enrichment_compute_resource**](CloudClientApi.md#get_project_enrichment_compute_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/compute | 
[**get_project_enrichments**](CloudClientApi.md#get_project_enrichments) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments | List all project enrichments
[**get_project_events_resource**](CloudClientApi.md#get_project_events_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/events/ | Returns a project&#39;s events with {project_id}
[**get_project_recording_events_resource**](CloudClientApi.md#get_project_recording_events_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events | Returns a project&#39;s recording event with {project_id} and {recording_id}
[**get_project_recordings_resource**](CloudClientApi.md#get_project_recordings_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/recordings/ | Returns a project&#39;s recordings with {project_id}
[**get_project_resource**](CloudClientApi.md#get_project_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id} | Returns a project with {project_id}
[**get_project_unique_events**](CloudClientApi.md#get_project_unique_events) | **GET** /workspaces/{workspace_id}/projects/{project_id}/unique-events/ | Returns all unique events in a project
[**get_projects_resource**](CloudClientApi.md#get_projects_resource) | **GET** /workspaces/{workspace_id}/projects/ | List all projects
[**get_recording**](CloudClientApi.md#get_recording) | **GET** /workspaces/{workspace_id}/recordings/{recording_id} | Returns a recording with {recording_id}
[**get_recording_blinks**](CloudClientApi.md#get_recording_blinks) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/blinks.json | Recording blinks
[**get_recording_blinks_timeline**](CloudClientApi.md#get_recording_blinks_timeline) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/blinks_timeline | Recording blinks timeline
[**get_recording_events**](CloudClientApi.md#get_recording_events) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/events | List recording events
[**get_recording_face_detections**](CloudClientApi.md#get_recording_face_detections) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/face_detections | Recording face detections
[**get_recording_face_detections_timeline**](CloudClientApi.md#get_recording_face_detections_timeline) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/face_detections_timeline | Recording face detections
[**get_recording_files**](CloudClientApi.md#get_recording_files) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/files | List recording files
[**get_recording_fixations**](CloudClientApi.md#get_recording_fixations) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/fixations.json | Recording fixations
[**get_recording_fixations_timeline**](CloudClientApi.md#get_recording_fixations_timeline) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/fixations_timeline | Recording fixations timeline
[**get_recording_gaze**](CloudClientApi.md#get_recording_gaze) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/gaze.{format} | temporary endpoint for player development
[**get_recording_scanpath**](CloudClientApi.md#get_recording_scanpath) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/scanpath.{format} | Get list of fixation scanpath points per world frame
[**get_recording_scene_camera_intrinsics**](CloudClientApi.md#get_recording_scene_camera_intrinsics) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/scene_camera.{format} | Get Recording&#39;s Scene Camera Intrinsics
[**get_recordings**](CloudClientApi.md#get_recordings) | **GET** /workspaces/{workspace_id}/recordings/ | List all recordings
[**get_recordings_events_resource**](CloudClientApi.md#get_recordings_events_resource) | **GET** /workspaces/{workspace_id}/recordings:unique-events | 
[**get_render**](CloudClientApi.md#get_render) | **GET** /workspaces/{workspace_id}/render/{render_definition_id} | Get a render enrichment
[**get_static_image_mapper_enrichment**](CloudClientApi.md#get_static_image_mapper_enrichment) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{static_enrichment_id} | Get a static image mapper enrichment
[**get_static_image_mapper_enrichments**](CloudClientApi.md#get_static_image_mapper_enrichments) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/ | List all static image mapper enrichments of a project
[**get_static_image_mapper_enrichments_recording_fixations**](CloudClientApi.md#get_static_image_mapper_enrichments_recording_fixations) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations | List all the fixations of a recording&#39;s static image mapper enrichments
[**get_surface**](CloudClientApi.md#get_surface) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id} | Return surface definition
[**get_surface_corners**](CloudClientApi.md#get_surface_corners) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/surface_corners | get surface locations for surface enrichment
[**get_surface_detections_timeline**](CloudClientApi.md#get_surface_detections_timeline) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/recordings/{recording_id}/gaze_in_aoi_timeline | Recording surface detections
[**get_surface_gaze_on_aoi**](CloudClientApi.md#get_surface_gaze_on_aoi) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/gaze_in_aoi | get gaze on aoi data for markerless enrichment
[**get_template**](CloudClientApi.md#get_template) | **GET** /workspaces/{workspace_id}/templates/{template_id} | Returns a template with {template_id}
[**get_templates**](CloudClientApi.md#get_templates) | **GET** /workspaces/{workspace_id}/templates/ | List all templates
[**get_token**](CloudClientApi.md#get_token) | **GET** /auth/tokens/{token_id} | Get an access token
[**get_tokens**](CloudClientApi.md#get_tokens) | **GET** /auth/tokens | Get all access tokens
[**get_visualization_config**](CloudClientApi.md#get_visualization_config) | **GET** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs/{visualization_config_id} | Get a visualization config
[**get_visualization_configs**](CloudClientApi.md#get_visualization_configs) | **GET** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs | List project&#39;s visualization configs
[**get_wearer**](CloudClientApi.md#get_wearer) | **GET** /workspaces/{workspace_id}/wearers/{wearer_id} | Returns a wearer with {wearer_id}
[**get_wearers**](CloudClientApi.md#get_wearers) | **GET** /workspaces/{workspace_id}/wearers/ | List all wearers
[**get_workspace**](CloudClientApi.md#get_workspace) | **GET** /workspaces/{workspace_id} | Returns the workspace with {workspace_id}
[**get_workspace_invitation**](CloudClientApi.md#get_workspace_invitation) | **GET** /auth/profile/invites/{token} | get workspace inviation for token
[**get_workspace_invitation_0**](CloudClientApi.md#get_workspace_invitation_0) | **GET** /workspaces/{workspace_id}/invites/{token} | Get workspace invitation for token
[**get_workspace_invitations**](CloudClientApi.md#get_workspace_invitations) | **GET** /auth/profile/invites | List all workspace inviations for current user
[**get_workspace_member**](CloudClientApi.md#get_workspace_member) | **GET** /workspaces/{workspace_id}/members/{user_id} | Get workspace member
[**get_workspace_members**](CloudClientApi.md#get_workspace_members) | **GET** /workspaces/{workspace_id}/members | List all members of workspace {workspace_id}
[**get_workspaces**](CloudClientApi.md#get_workspaces) | **GET** /workspaces/ | List all workspaces for a user
[**initialize_markerless**](CloudClientApi.md#initialize_markerless) | **POST** /workspaces/{workspace_id}/markerless/ | Create markerless definition
[**initialize_rendering**](CloudClientApi.md#initialize_rendering) | **POST** /workspaces/{workspace_id}/render/ | Create world render definition
[**list_workspace_invitations**](CloudClientApi.md#list_workspace_invitations) | **GET** /workspaces/{workspace_id}/invites | List workspace invitations
[**patch_aoi**](CloudClientApi.md#patch_aoi) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois/{aoi_id} | Update an aoi
[**patch_filter**](CloudClientApi.md#patch_filter) | **PATCH** /workspaces/{workspace_id}/filters/{filter_id} | Update a filter
[**patch_label**](CloudClientApi.md#patch_label) | **PATCH** /workspaces/{workspace_id}/labels/{label_id} | Update a label
[**patch_profile**](CloudClientApi.md#patch_profile) | **PATCH** /auth/profile | Update user profile
[**patch_project_enrichment_resource**](CloudClientApi.md#patch_project_enrichment_resource) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id} | Update a project enrichment
[**patch_project_recording_event_resource**](CloudClientApi.md#patch_project_recording_event_resource) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events/{event_id} | Update a project recording event
[**patch_project_resource**](CloudClientApi.md#patch_project_resource) | **PATCH** /workspaces/{workspace_id}/projects/{project_id} | Update a project
[**patch_recording**](CloudClientApi.md#patch_recording) | **PATCH** /workspaces/{workspace_id}/recordings/{recording_id} | Update a recording
[**patch_recording_event_resource**](CloudClientApi.md#patch_recording_event_resource) | **PATCH** /workspaces/{workspace_id}/recordings/{recording_id}/events/{event_id} | Update a recording event
[**patch_render**](CloudClientApi.md#patch_render) | **PATCH** /workspaces/{workspace_id}/render/{render_definition_id} | Update a render enrichment
[**patch_rotate_surface_orientation**](CloudClientApi.md#patch_rotate_surface_orientation) | **PATCH** /workspaces/{workspace_id}/surfaces/{surface_id}/rotate | Change surface rotation
[**patch_static_image_mapper_enrichment**](CloudClientApi.md#patch_static_image_mapper_enrichment) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{static_enrichment_id} | Update a static image mapper enrichment
[**patch_surface**](CloudClientApi.md#patch_surface) | **PATCH** /workspaces/{workspace_id}/surfaces/{surface_id} | Update surface definition
[**patch_template**](CloudClientApi.md#patch_template) | **PATCH** /workspaces/{workspace_id}/templates/{template_id} | Update a template
[**patch_visualization_config**](CloudClientApi.md#patch_visualization_config) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs/{visualization_config_id} | Update a visualization config
[**patch_wearer**](CloudClientApi.md#patch_wearer) | **PATCH** /workspaces/{workspace_id}/wearers/{wearer_id} | Update a wearer
[**patch_workspace_member**](CloudClientApi.md#patch_workspace_member) | **PATCH** /workspaces/{workspace_id}/members/{user_id} | Patch members of workspace {workspace_id}
[**post_accept_invitation_resource**](CloudClientApi.md#post_accept_invitation_resource) | **POST** /auth/profile/invites/{token}/accept | Create workspace member based on invite token
[**post_aoi**](CloudClientApi.md#post_aoi) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois | Create a new aoi
[**post_aoi_0**](CloudClientApi.md#post_aoi_0) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois/{aoi_id} | Create a new aoi
[**post_aoi_1**](CloudClientApi.md#post_aoi_1) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/aois:stats | Create a new aoi
[**post_distorted_surface_location**](CloudClientApi.md#post_distorted_surface_location) | **POST** /workspaces/{workspace_id}/surfaces/{surface_id}/set_distorted_location_using_recording | Set distorted surface corner locations
[**post_download_heatmap**](CloudClientApi.md#post_download_heatmap) | **POST** /workspaces/{workspace_id}/heatmap/zip_download | download zip file with heatmaps
[**post_filters**](CloudClientApi.md#post_filters) | **POST** /workspaces/{workspace_id}/filters/ | Create a new filter
[**post_heatmap**](CloudClientApi.md#post_heatmap) | **POST** /workspaces/{workspace_id}/heatmap/ | get heatmap image or json data
[**post_label**](CloudClientApi.md#post_label) | **POST** /workspaces/{workspace_id}/labels/ | Create a new label
[**post_label_0**](CloudClientApi.md#post_label_0) | **POST** /workspaces/{workspace_id}/labels/{label_id} | Create a new label
[**post_login**](CloudClientApi.md#post_login) | **POST** /auth/login | Login the user and return a new session cookie
[**post_logout**](CloudClientApi.md#post_logout) | **POST** /auth/logout | Logout the current user
[**post_project_download_resource**](CloudClientApi.md#post_project_download_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/download | Download project data
[**post_project_enrichment**](CloudClientApi.md#post_project_enrichment) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments | Create a new project enrichment
[**post_project_enrichment_cancel_resource**](CloudClientApi.md#post_project_enrichment_cancel_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/cancel | 
[**post_project_enrichment_compute_resource**](CloudClientApi.md#post_project_enrichment_compute_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/compute | 
[**post_project_enrichment_export_resource**](CloudClientApi.md#post_project_enrichment_export_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/export | Export an enrichment data
[**post_project_recording_events_resource**](CloudClientApi.md#post_project_recording_events_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events | Create a new project recording event
[**post_projects_resource**](CloudClientApi.md#post_projects_resource) | **POST** /workspaces/{workspace_id}/projects/ | Create a new project
[**post_recording_event**](CloudClientApi.md#post_recording_event) | **POST** /workspaces/{workspace_id}/recordings/{recording_id}/events | Create a new recording event
[**post_static_image_mapper_enrichment**](CloudClientApi.md#post_static_image_mapper_enrichment) | **POST** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/ | Create a new static image mapper enrichment
[**post_surface**](CloudClientApi.md#post_surface) | **POST** /workspaces/{workspace_id}/surfaces/ | Create a new surface definition
[**post_template**](CloudClientApi.md#post_template) | **POST** /workspaces/{workspace_id}/templates/ | Create a new template
[**post_token**](CloudClientApi.md#post_token) | **POST** /auth/tokens | Creates a new access token
[**post_unregister**](CloudClientApi.md#post_unregister) | **POST** /auth/unregister | Unregisters the currently logged in user
[**post_visualization_config**](CloudClientApi.md#post_visualization_config) | **POST** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs | Create a new visualization config
[**post_wearer**](CloudClientApi.md#post_wearer) | **POST** /workspaces/{workspace_id}/wearers/ | Create a new wearer
[**post_workspace**](CloudClientApi.md#post_workspace) | **POST** /workspaces/ | Create a new workspace
[**post_workspace_members_resource**](CloudClientApi.md#post_workspace_members_resource) | **POST** /workspaces/{workspace_id}/members | Add workspace member
[**project_enrichments_export**](CloudClientApi.md#project_enrichments_export) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/export | Export an enrichment data
[**put_static_image_mapper_enrichments_recording_fixation**](CloudClientApi.md#put_static_image_mapper_enrichments_recording_fixation) | **PUT** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations/{fixation_id} | Insert or update coordinates of a particular fixation of recording&#39;s
[**scan_markerless**](CloudClientApi.md#scan_markerless) | **POST** /workspaces/{workspace_id}/markerless/{markerless_id}/scan | Scan markerless
[**update_workspace**](CloudClientApi.md#update_workspace) | **PATCH** /workspaces/{workspace_id} | Update a workspace


# **clear_static_image_mapper_enrichments_recording_fixation**
> clear_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id)

Clear or resets all the mapped fixation of recording's

static image mapper enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 

    try:
        # Clear or resets all the mapped fixation of recording's
        await api_instance.clear_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->clear_static_image_mapper_enrichments_recording_fixation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cleared manually mapped fixation data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Enrichment or Recording is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recording_event**
> RecordingEventCreateResponse create_recording_event(workspace_id, recording_id, format, payload)

Create recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.create_recording_event import CreateRecordingEvent
from pupilcloud.models.recording_event_create_response import RecordingEventCreateResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    payload = pupilcloud.CreateRecordingEvent() # CreateRecordingEvent | 

    try:
        # Create recording event
        api_response = await api_instance.create_recording_event(workspace_id, recording_id, format, payload)
        print("The response of CloudClientApi->create_recording_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->create_recording_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **payload** | [**CreateRecordingEvent**](CreateRecordingEvent.md)|  | 

### Return type

[**RecordingEventCreateResponse**](RecordingEventCreateResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created recording event |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_invitation**
> WorkspaceInvitationCreateResponse create_workspace_invitation(workspace_id, payload)

Create a workspace invitation

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_invitation_create_response import WorkspaceInvitationCreateResponse
from pupilcloud.models.workspace_invitation_post_request import WorkspaceInvitationPostRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.WorkspaceInvitationPostRequest() # WorkspaceInvitationPostRequest | 

    try:
        # Create a workspace invitation
        api_response = await api_instance.create_workspace_invitation(workspace_id, payload)
        print("The response of CloudClientApi->create_workspace_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->create_workspace_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**WorkspaceInvitationPostRequest**](WorkspaceInvitationPostRequest.md)|  | 

### Return type

[**WorkspaceInvitationCreateResponse**](WorkspaceInvitationCreateResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace invitations |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Workspace doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aoi**
> delete_aoi(workspace_id, project_id, enrichment_id, aoi_id)

Delete an aoi

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    aoi_id = 'aoi_id_example' # str | 

    try:
        # Delete an aoi
        await api_instance.delete_aoi(workspace_id, project_id, enrichment_id, aoi_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **aoi_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aois**
> delete_aois(workspace_id, project_id, enrichment_id, payload)

Delete multiple aois

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aois_delete_request import AoisDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.AoisDeleteRequest() # AoisDeleteRequest | 

    try:
        # Delete multiple aois
        await api_instance.delete_aois(workspace_id, project_id, enrichment_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_aois: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**AoisDeleteRequest**](AoisDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aois_0**
> delete_aois_0(workspace_id, project_id, enrichment_id, payload)

Delete multiple aois

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aois_delete_request import AoisDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.AoisDeleteRequest() # AoisDeleteRequest | 

    try:
        # Delete multiple aois
        await api_instance.delete_aois_0(workspace_id, project_id, enrichment_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_aois_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**AoisDeleteRequest**](AoisDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> delete_filter(workspace_id, filter_id)

Delete a filter

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    filter_id = 'filter_id_example' # str | 

    try:
        # Delete a filter
        await api_instance.delete_filter(workspace_id, filter_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **filter_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filters**
> delete_filters(workspace_id, payload)

Delete multiple filters

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.filters_delete_request import FiltersDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.FiltersDeleteRequest() # FiltersDeleteRequest | 

    try:
        # Delete multiple filters
        await api_instance.delete_filters(workspace_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**FiltersDeleteRequest**](FiltersDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_label**
> delete_label(workspace_id, label_id)

Delete a label

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    label_id = 'label_id_example' # str | 

    try:
        # Delete a label
        await api_instance.delete_label(workspace_id, label_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **label_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_labels**
> delete_labels(workspace_id, payload)

Delete multiple labels

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.labels_delete_request import LabelsDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.LabelsDeleteRequest() # LabelsDeleteRequest | 

    try:
        # Delete multiple labels
        await api_instance.delete_labels(workspace_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**LabelsDeleteRequest**](LabelsDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_enrichment_resource**
> delete_project_enrichment_resource(workspace_id, project_id, enrichment_id)

Delete a project enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        # Delete a project enrichment
        await api_instance.delete_project_enrichment_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_project_enrichment_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_recording_event_resource**
> delete_project_recording_event_resource(workspace_id, project_id, recording_id, event_id)

Delete a project recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 

    try:
        # Delete a project recording event
        await api_instance.delete_project_recording_event_resource(workspace_id, project_id, recording_id, event_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_project_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_resource**
> delete_project_resource(workspace_id, project_id)

Delete a project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Delete a project
        await api_instance.delete_project_resource(workspace_id, project_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_projects_resource**
> delete_projects_resource(workspace_id, payload)

Delete multiple projects

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.projects_delete_request import ProjectsDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.ProjectsDeleteRequest() # ProjectsDeleteRequest | 

    try:
        # Delete multiple projects
        await api_instance.delete_projects_resource(workspace_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_projects_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**ProjectsDeleteRequest**](ProjectsDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording**
> delete_recording(workspace_id, recording_id)

Delete a recording

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # Delete a recording
        await api_instance.delete_recording(workspace_id, recording_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_event_resource**
> RecordingEventResourceDeleteResponse delete_recording_event_resource(workspace_id, recording_id, event_id)

Delete a recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_event_resource_delete_response import RecordingEventResourceDeleteResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 

    try:
        # Delete a recording event
        api_response = await api_instance.delete_recording_event_resource(workspace_id, recording_id, event_id)
        print("The response of CloudClientApi->delete_recording_event_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 

### Return type

[**RecordingEventResourceDeleteResponse**](RecordingEventResourceDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted event |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recordings**
> delete_recordings(workspace_id, payload)

Delete multiple recordings

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recordings_delete_request import RecordingsDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.RecordingsDeleteRequest() # RecordingsDeleteRequest | 

    try:
        # Delete multiple recordings
        await api_instance.delete_recordings(workspace_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**RecordingsDeleteRequest**](RecordingsDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_static_image_mapper_enrichments_recording_fixation**
> delete_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id)

Deletes coordinates of a particular fixation of recording's

static image mapper enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    fixation_id = 56 # int | 

    try:
        # Deletes coordinates of a particular fixation of recording's
        await api_instance.delete_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_static_image_mapper_enrichments_recording_fixation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **fixation_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource deleted |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Enrichment or Recording or fixations.json or event section or fixation coordinates are not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> TemplateDeleteResponse delete_template(workspace_id, template_id)

Delete a template

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.template_delete_response import TemplateDeleteResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    template_id = 'template_id_example' # str | 

    try:
        # Delete a template
        api_response = await api_instance.delete_template(workspace_id, template_id)
        print("The response of CloudClientApi->delete_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **template_id** | **str**|  | 

### Return type

[**TemplateDeleteResponse**](TemplateDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a single template |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**405** | Method not accepted eg. trying to delete default template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates**
> delete_templates(workspace_id, payload)

Delete multiple templates

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.templates_delete_request import TemplatesDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.TemplatesDeleteRequest() # TemplatesDeleteRequest | 

    try:
        # Delete multiple templates
        await api_instance.delete_templates(workspace_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**TemplatesDeleteRequest**](TemplatesDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**422** | Unprocessable entity eg. trying to delete default template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> TokenDeleteResponse delete_token(token_id)

Delete an access token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.token_delete_response import TokenDeleteResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    token_id = 'token_id_example' # str | 

    try:
        # Delete an access token
        api_response = await api_instance.delete_token(token_id)
        print("The response of CloudClientApi->delete_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 

### Return type

[**TokenDeleteResponse**](TokenDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_visualization_config**
> VisualizationConfigDeleteResponse delete_visualization_config(workspace_id, project_id, visualization_config_id)

Delete a visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_delete_response import VisualizationConfigDeleteResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    visualization_config_id = 'visualization_config_id_example' # str | 

    try:
        # Delete a visualization config
        api_response = await api_instance.delete_visualization_config(workspace_id, project_id, visualization_config_id)
        print("The response of CloudClientApi->delete_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **visualization_config_id** | **str**|  | 

### Return type

[**VisualizationConfigDeleteResponse**](VisualizationConfigDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a visualization config |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Visualization config not found |  -  |
**410** | Visualization config deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wearer**
> WearerDeleteResponse delete_wearer(workspace_id, wearer_id)

Delete a wearer

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.wearer_delete_response import WearerDeleteResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    wearer_id = 'wearer_id_example' # str | 

    try:
        # Delete a wearer
        api_response = await api_instance.delete_wearer(workspace_id, wearer_id)
        print("The response of CloudClientApi->delete_wearer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_wearer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **wearer_id** | **str**|  | 

### Return type

[**WearerDeleteResponse**](WearerDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a single wearer |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Wearer doesn&#39;t exist |  -  |
**410** | Wearer was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wearers**
> delete_wearers(workspace_id, payload)

Delete multiple wearers

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.wearers_delete_request import WearersDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.WearersDeleteRequest() # WearersDeleteRequest | 

    try:
        # Delete multiple wearers
        await api_instance.delete_wearers(workspace_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_wearers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**WearersDeleteRequest**](WearersDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> delete_workspace(workspace_id)

Delete a workspace

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # Delete a workspace
        await api_instance.delete_workspace(workspace_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;} |  -  |
**404** | Workspace doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_invitation**
> delete_workspace_invitation(token)

Delete a workspace invitation

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    token = 'token_example' # str | 

    try:
        # Delete a workspace invitation
        await api_instance.delete_workspace_invitation(token)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_workspace_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_invitation_0**
> delete_workspace_invitation_0(workspace_id, token)

Delete a workspace invitation

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    token = 'token_example' # str | 

    try:
        # Delete a workspace invitation
        await api_instance.delete_workspace_invitation_0(workspace_id, token)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_workspace_invitation_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_member**
> WorkspaceMemberDeleteResponse delete_workspace_member(workspace_id, user_id)

Delete a workspace member from a workspace

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_member_delete_response import WorkspaceMemberDeleteResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    user_id = 'user_id_example' # str | 

    try:
        # Delete a workspace member from a workspace
        api_response = await api_instance.delete_workspace_member(workspace_id, user_id)
        print("The response of CloudClientApi->delete_workspace_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->delete_workspace_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **user_id** | **str**|  | 

### Return type

[**WorkspaceMemberDeleteResponse**](WorkspaceMemberDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace members |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;OWNER&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Workspace member not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_raw_data_export_zip**
> bytearray download_raw_data_export_zip(workspace_id, ids=ids, exclude=exclude)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    ids = ['ids_example'] # List[str] | Recordings UUIDs for which data is to be exported (optional)
    exclude = ['exclude_example'] # List[str] | file to exclude (optional)

    try:
        api_response = await api_instance.download_raw_data_export_zip(workspace_id, ids=ids, exclude=exclude)
        print("The response of CloudClientApi->download_raw_data_export_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->download_raw_data_export_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **ids** | [**List[str]**](str.md)| Recordings UUIDs for which data is to be exported | [optional] 
 **exclude** | [**List[str]**](str.md)| file to exclude | [optional] 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording raw data export zip file archive |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recording_file**
> bytearray download_recording_file(workspace_id, recording_id, filename)

Download a recording's file

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    filename = 'filename_example' # str | 

    try:
        # Download a recording's file
        api_response = await api_instance.download_recording_file(workspace_id, recording_id, filename)
        print("The response of CloudClientApi->download_recording_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->download_recording_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **filename** | **str**|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**302** | Redirection url to download file |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recording_zip**
> bytearray download_recording_zip(workspace_id, recording_id)

Download recording files as a zip file

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # Download recording files as a zip file
        api_response = await api_instance.download_recording_zip(workspace_id, recording_id)
        print("The response of CloudClientApi->download_recording_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->download_recording_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording as a zip file archive |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recordings_zip**
> download_recordings_zip(workspace_id, ids=ids)

Download multiple recordings in zip archive

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    ids = ['ids_example'] # List[str] | recording ids to download (optional)

    try:
        # Download multiple recordings in zip archive
        await api_instance.download_recordings_zip(workspace_id, ids=ids)
    except Exception as e:
        print("Exception when calling CloudClientApi->download_recordings_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **ids** | [**List[str]**](str.md)| recording ids to download | [optional] 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recordings as a zip file archive |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_static_image_mapper_enrichment**
> export_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)

Export static image mapper enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    static_enrichment_id = 'static_enrichment_id_example' # str | 

    try:
        # Export static image mapper enrichment
        await api_instance.export_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->export_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **static_enrichment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Static image mapper enrichment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aoi**
> AoiGetResponse get_aoi(workspace_id, project_id, enrichment_id, aoi_id)

Returns an aoi with {aoi_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aoi_get_response import AoiGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    aoi_id = 'aoi_id_example' # str | 

    try:
        # Returns an aoi with {aoi_id}
        api_response = await api_instance.get_aoi(workspace_id, project_id, enrichment_id, aoi_id)
        print("The response of CloudClientApi->get_aoi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **aoi_id** | **str**|  | 

### Return type

[**AoiGetResponse**](AoiGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single Aoi |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aoi_stats**
> get_aoi_stats(workspace_id, project_id, enrichment_id, rids=rids)

List all aois of an enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    rids = ['rids_example'] # List[str] | Recordings UUIDs for which aoi stats is to be provided (optional)

    try:
        # List all aois of an enrichment
        await api_instance.get_aoi_stats(workspace_id, project_id, enrichment_id, rids=rids)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_aoi_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **rids** | [**List[str]**](str.md)| Recordings UUIDs for which aoi stats is to be provided | [optional] 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aois**
> AoisGetResponse get_aois(workspace_id, project_id, enrichment_id)

List all aois of an enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aois_get_response import AoisGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        # List all aois of an enrichment
        api_response = await api_instance.get_aois(workspace_id, project_id, enrichment_id)
        print("The response of CloudClientApi->get_aois:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_aois: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

### Return type

[**AoisGetResponse**](AoisGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of aois |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apriltag_detections**
> ApriltagDetectionsGetResponse get_apriltag_detections(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect)

Get apritag data for surface enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.apriltag_detections_get_response import ApriltagDetectionsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | 
    end = 3.4 # float |  (optional)
    detect = 0 # int |  (optional) (default to 0)

    try:
        # Get apritag data for surface enrichment
        api_response = await api_instance.get_apriltag_detections(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect)
        print("The response of CloudClientApi->get_apriltag_detections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_apriltag_detections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **start** | **float**|  | 
 **end** | **float**|  | [optional] 
 **detect** | **int**|  | [optional] [default to 0]

### Return type

[**ApriltagDetectionsGetResponse**](ApriltagDetectionsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of apriltag detections |  -  |
**400** | Enrichment doesn&#39;t belong to surface id |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Surface definition not found |  -  |
**405** | Project enrichment dosn&#39;t support surfaces |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apriltags_at_timestamp**
> ApriltagsAtTimestampGetResponse get_apriltags_at_timestamp(workspace_id, recording_id, timestamp=timestamp, with_duplicates=with_duplicates)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.apriltags_at_timestamp_get_response import ApriltagsAtTimestampGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    timestamp = None # object | timestamp offset in recording in seconds (optional)
    with_duplicates = True # bool | return duplicate apriltags (defaults to best) (optional)

    try:
        api_response = await api_instance.get_apriltags_at_timestamp(workspace_id, recording_id, timestamp=timestamp, with_duplicates=with_duplicates)
        print("The response of CloudClientApi->get_apriltags_at_timestamp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_apriltags_at_timestamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **timestamp** | [**object**](.md)| timestamp offset in recording in seconds | [optional] 
 **with_duplicates** | **bool**| return duplicate apriltags (defaults to best) | [optional] 

### Return type

[**ApriltagsAtTimestampGetResponse**](ApriltagsAtTimestampGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apriltags in frame |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canny_sso_token**
> CannySsoTokenGetResponse get_canny_sso_token()

Returns the canny

io SSO token for current user

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.canny_sso_token_get_response import CannySsoTokenGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)

    try:
        # Returns the canny
        api_response = await api_instance.get_canny_sso_token()
        print("The response of CloudClientApi->get_canny_sso_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_canny_sso_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CannySsoTokenGetResponse**](CannySsoTokenGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Canny sso token |  -  |
**401** | Unauthorized / invalid credentials / cookie expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_heatmap**
> bytearray get_download_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)

download zip file with heatmaps

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_ids = ['recording_ids_example'] # List[str] | Recordings UUIDs for which heatmap data is to be retrieved (optional)
    n_bins = 300 # int |  (optional) (default to 300)
    sigma = 0.05 # float |  (optional) (default to 0.05)
    height = 512 # int |  (optional) (default to 512)
    width = 512 # int |  (optional) (default to 512)
    max_size = 56 # int |  (optional)
    colormap = Turbo # str |  (optional) (default to Turbo)
    var_json = False # bool |  (optional) (default to False)

    try:
        # download zip file with heatmaps
        api_response = await api_instance.get_download_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)
        print("The response of CloudClientApi->get_download_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_download_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_ids** | [**List[str]**](str.md)| Recordings UUIDs for which heatmap data is to be retrieved | [optional] 
 **n_bins** | **int**|  | [optional] [default to 300]
 **sigma** | **float**|  | [optional] [default to 0.05]
 **height** | **int**|  | [optional] [default to 512]
 **width** | **int**|  | [optional] [default to 512]
 **max_size** | **int**|  | [optional] 
 **colormap** | **str**|  | [optional] [default to Turbo]
 **var_json** | **bool**|  | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter**
> FilterGetResponse get_filter(workspace_id, filter_id)

Returns a filter with {filter_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.filter_get_response import FilterGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    filter_id = 'filter_id_example' # str | 

    try:
        # Returns a filter with {filter_id}
        api_response = await api_instance.get_filter(workspace_id, filter_id)
        print("The response of CloudClientApi->get_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **filter_id** | **str**|  | 

### Return type

[**FilterGetResponse**](FilterGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single filter |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters**
> FiltersGetResponse get_filters(workspace_id)

List all filters

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.filters_get_response import FiltersGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List all filters
        api_response = await api_instance.get_filters(workspace_id)
        print("The response of CloudClientApi->get_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**FiltersGetResponse**](FiltersGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of filters |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware**
> bytearray get_hardware(serial_number, version, var_json=var_json)

Returns calibration

{version} data for hardware with {serial_number}

### Example


```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)


# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    serial_number = 'serial_number_example' # str | 
    version = 'version_example' # str | 
    var_json = 'var_json_example' # str | Specify to get result in json format (optional)

    try:
        # Returns calibration
        api_response = await api_instance.get_hardware(serial_number, version, var_json=var_json)
        print("The response of CloudClientApi->get_hardware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_hardware: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**|  | 
 **version** | **str**|  | 
 **var_json** | **str**| Specify to get result in json format | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hardware data |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap**
> bytearray get_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)

get heatmap image or json data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_ids = ['recording_ids_example'] # List[str] | Recordings UUIDs for which heatmap data is to be retrieved (optional)
    n_bins = 300 # int |  (optional) (default to 300)
    sigma = 0.05 # float |  (optional) (default to 0.05)
    height = 512 # int |  (optional) (default to 512)
    width = 512 # int |  (optional) (default to 512)
    max_size = 56 # int |  (optional)
    colormap = Turbo # str |  (optional) (default to Turbo)
    var_json = False # bool |  (optional) (default to False)

    try:
        # get heatmap image or json data
        api_response = await api_instance.get_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)
        print("The response of CloudClientApi->get_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_ids** | [**List[str]**](str.md)| Recordings UUIDs for which heatmap data is to be retrieved | [optional] 
 **n_bins** | **int**|  | [optional] [default to 300]
 **sigma** | **float**|  | [optional] [default to 0.05]
 **height** | **int**|  | [optional] [default to 512]
 **width** | **int**|  | [optional] [default to 512]
 **max_size** | **int**|  | [optional] 
 **colormap** | **str**|  | [optional] [default to Turbo]
 **var_json** | **bool**|  | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap_background**
> bytearray get_heatmap_background(workspace_id, project_id, enrichment_id, max_size=max_size)

get heatmap background for overlay

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    max_size = 512 # int |  (optional) (default to 512)

    try:
        # get heatmap background for overlay
        api_response = await api_instance.get_heatmap_background(workspace_id, project_id, enrichment_id, max_size=max_size)
        print("The response of CloudClientApi->get_heatmap_background:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_heatmap_background: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **max_size** | **int**|  | [optional] [default to 512]

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_label**
> LabelGetResponse get_label(workspace_id, label_id)

Returns a label with {label_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.label_get_response import LabelGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    label_id = 'label_id_example' # str | 

    try:
        # Returns a label with {label_id}
        api_response = await api_instance.get_label(workspace_id, label_id)
        print("The response of CloudClientApi->get_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **label_id** | **str**|  | 

### Return type

[**LabelGetResponse**](LabelGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single label |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_labels**
> LabelsGetResponse get_labels(workspace_id)

List all labels

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.labels_get_response import LabelsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List all labels
        api_response = await api_instance.get_labels(workspace_id)
        print("The response of CloudClientApi->get_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**LabelsGetResponse**](LabelsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of labels |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless**
> MarkerlessGetResponse get_markerless(workspace_id, markerless_id)

Get markerless definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_get_response import MarkerlessGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 

    try:
        # Get markerless definition
        api_response = await api_instance.get_markerless(workspace_id, markerless_id)
        print("The response of CloudClientApi->get_markerless:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_markerless: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 

### Return type

[**MarkerlessGetResponse**](MarkerlessGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Markerless scanning definition |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Markerless definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_camera_poses**
> MarkerlessCameraPosesGetResponse get_markerless_camera_poses(workspace_id, markerless_id, recording_id, format, start=start, end=end, limit=limit)

get markerless camera poses

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_camera_poses_get_response import MarkerlessCameraPosesGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    limit = 56 # int |  (optional)

    try:
        # get markerless camera poses
        api_response = await api_instance.get_markerless_camera_poses(workspace_id, markerless_id, recording_id, format, start=start, end=end, limit=limit)
        print("The response of CloudClientApi->get_markerless_camera_poses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_markerless_camera_poses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**MarkerlessCameraPosesGetResponse**](MarkerlessCameraPosesGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of markerless camera pose |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_detections_timeline**
> MarkerlessDetectionsTimelineGetResponse get_markerless_detections_timeline(workspace_id, markerless_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)

Recording markerless detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_detections_timeline_get_response import MarkerlessDetectionsTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    recording_id2 = 'recording_id_example' # str | recording id
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording markerless detections
        api_response = await api_instance.get_markerless_detections_timeline(workspace_id, markerless_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)
        print("The response of CloudClientApi->get_markerless_detections_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_markerless_detections_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **recording_id2** | **str**| recording id | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**MarkerlessDetectionsTimelineGetResponse**](MarkerlessDetectionsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of markerless detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_gaze_on_aoi**
> MarkerlessGazeOnAoiGetResponse get_markerless_gaze_on_aoi(workspace_id, markerless_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)

get gaze on aoi data for markerless enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_gaze_on_aoi_get_response import MarkerlessGazeOnAoiGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    project_id = 'project_id_example' # str |  (optional)
    enrichment_id = 'enrichment_id_example' # str |  (optional)
    recording_id = 'recording_id_example' # str |  (optional)
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)

    try:
        # get gaze on aoi data for markerless enrichment
        api_response = await api_instance.get_markerless_gaze_on_aoi(workspace_id, markerless_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)
        print("The response of CloudClientApi->get_markerless_gaze_on_aoi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_markerless_gaze_on_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **project_id** | **str**|  | [optional] 
 **enrichment_id** | **str**|  | [optional] 
 **recording_id** | **str**|  | [optional] 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 

### Return type

[**MarkerlessGazeOnAoiGetResponse**](MarkerlessGazeOnAoiGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of gaze in aoi coordinates with time ranges |  -  |
**400** | Enrichment doesn&#39;t belong to markerless id |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Markerless definition not found |  -  |
**405** | Enrichment does not support markerless |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_point_cloud**
> MarkerlessPointCloudGetResponse get_markerless_point_cloud(workspace_id, markerless_id, format, limit=limit)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_point_cloud_get_response import MarkerlessPointCloudGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    format = 'format_example' # str | 
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.get_markerless_point_cloud(workspace_id, markerless_id, format, limit=limit)
        print("The response of CloudClientApi->get_markerless_point_cloud:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_markerless_point_cloud: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **format** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**MarkerlessPointCloudGetResponse**](MarkerlessPointCloudGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of markerless point cloud |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> ProfileGetResponse get_profile()

Returns the current logged in user based on auth token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.profile_get_response import ProfileGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)

    try:
        # Returns the current logged in user based on auth token
        api_response = await api_instance.get_profile()
        print("The response of CloudClientApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProfileGetResponse**](ProfileGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current user |  -  |
**401** | Unauthorized / invalid credentials / cookie expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_enrichment**
> ProjectEnrichmentGetResponse get_project_enrichment(workspace_id, project_id, enrichment_id)

Get a project enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_get_response import ProjectEnrichmentGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        # Get a project enrichment
        api_response = await api_instance.get_project_enrichment(workspace_id, project_id, enrichment_id)
        print("The response of CloudClientApi->get_project_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

### Return type

[**ProjectEnrichmentGetResponse**](ProjectEnrichmentGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project enrichment |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_enrichment_compute_resource**
> get_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        await api_instance.get_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_enrichment_compute_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_enrichments**
> ProjectEnrichmentsGetResponse get_project_enrichments(workspace_id, project_id)

List all project enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichments_get_response import ProjectEnrichmentsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # List all project enrichments
        api_response = await api_instance.get_project_enrichments(workspace_id, project_id)
        print("The response of CloudClientApi->get_project_enrichments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_enrichments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectEnrichmentsGetResponse**](ProjectEnrichmentsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of project enrichments |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_events_resource**
> ProjectEventsResourceGetResponse get_project_events_resource(workspace_id, project_id)

Returns a project's events with {project_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_events_resource_get_response import ProjectEventsResourceGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns a project's events with {project_id}
        api_response = await api_instance.get_project_events_resource(workspace_id, project_id)
        print("The response of CloudClientApi->get_project_events_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectEventsResourceGetResponse**](ProjectEventsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project recording events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_recording_events_resource**
> ProjectRecordingEventsResourceGetResponse get_project_recording_events_resource(workspace_id, project_id, recording_id)

Returns a project's recording event with {project_id} and {recording_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recording_events_resource_get_response import ProjectRecordingEventsResourceGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 

    try:
        # Returns a project's recording event with {project_id} and {recording_id}
        api_response = await api_instance.get_project_recording_events_resource(workspace_id, project_id, recording_id)
        print("The response of CloudClientApi->get_project_recording_events_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_recording_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 

### Return type

[**ProjectRecordingEventsResourceGetResponse**](ProjectRecordingEventsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project&#39;s recording events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_recordings_resource**
> ProjectRecordingsResourceGetResponse get_project_recordings_resource(workspace_id, project_id)

Returns a project's recordings with {project_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recordings_resource_get_response import ProjectRecordingsResourceGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns a project's recordings with {project_id}
        api_response = await api_instance.get_project_recordings_resource(workspace_id, project_id)
        print("The response of CloudClientApi->get_project_recordings_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_recordings_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectRecordingsResourceGetResponse**](ProjectRecordingsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project&#39;s recordings |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_resource**
> ProjectResourceGetResponse get_project_resource(workspace_id, project_id)

Returns a project with {project_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_resource_get_response import ProjectResourceGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns a project with {project_id}
        api_response = await api_instance.get_project_resource(workspace_id, project_id)
        print("The response of CloudClientApi->get_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectResourceGetResponse**](ProjectResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single project |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_unique_events**
> ProjectUniqueEventsGetResponse get_project_unique_events(workspace_id, project_id)

Returns all unique events in a project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_unique_events_get_response import ProjectUniqueEventsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns all unique events in a project
        api_response = await api_instance.get_project_unique_events(workspace_id, project_id)
        print("The response of CloudClientApi->get_project_unique_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_project_unique_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectUniqueEventsGetResponse**](ProjectUniqueEventsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project&#39;s unique events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_resource**
> ProjectsResourceGetResponse get_projects_resource(workspace_id)

List all projects

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.projects_resource_get_response import ProjectsResourceGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List all projects
        api_response = await api_instance.get_projects_resource(workspace_id)
        print("The response of CloudClientApi->get_projects_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_projects_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**ProjectsResourceGetResponse**](ProjectsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of projects |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording**
> RecordingGetResponse get_recording(workspace_id, recording_id)

Returns a recording with {recording_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_get_response import RecordingGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # Returns a recording with {recording_id}
        api_response = await api_instance.get_recording(workspace_id, recording_id)
        print("The response of CloudClientApi->get_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

[**RecordingGetResponse**](RecordingGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single recording |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Recording doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_blinks**
> RecordingBlinksGetResponse get_recording_blinks(workspace_id, recording_id, start=start, end=end)

Recording blinks

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_blinks_get_response import RecordingBlinksGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)

    try:
        # Recording blinks
        api_response = await api_instance.get_recording_blinks(workspace_id, recording_id, start=start, end=end)
        print("The response of CloudClientApi->get_recording_blinks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_blinks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 

### Return type

[**RecordingBlinksGetResponse**](RecordingBlinksGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording blinks |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_blinks_timeline**
> RecordingBlinksTimelineGetResponse get_recording_blinks_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)

Recording blinks timeline

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_blinks_timeline_get_response import RecordingBlinksTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording blinks timeline
        api_response = await api_instance.get_recording_blinks_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)
        print("The response of CloudClientApi->get_recording_blinks_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_blinks_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**RecordingBlinksTimelineGetResponse**](RecordingBlinksTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of blinks |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_events**
> RecordingEventsGetResponse get_recording_events(workspace_id, recording_id)

List recording events

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_events_get_response import RecordingEventsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # List recording events
        api_response = await api_instance.get_recording_events(workspace_id, recording_id)
        print("The response of CloudClientApi->get_recording_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

[**RecordingEventsGetResponse**](RecordingEventsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recording events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_face_detections**
> RecordingFaceDetectionsGetResponse get_recording_face_detections(workspace_id, recording_id, start=start, end=end, with_landmarks=with_landmarks)

Recording face detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_face_detections_get_response import RecordingFaceDetectionsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    with_landmarks = True # bool |  (optional)

    try:
        # Recording face detections
        api_response = await api_instance.get_recording_face_detections(workspace_id, recording_id, start=start, end=end, with_landmarks=with_landmarks)
        print("The response of CloudClientApi->get_recording_face_detections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_face_detections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **with_landmarks** | **bool**|  | [optional] 

### Return type

[**RecordingFaceDetectionsGetResponse**](RecordingFaceDetectionsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of face detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_face_detections_timeline**
> RecordingFaceDetectionsTimelineGetResponse get_recording_face_detections_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)

Recording face detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_face_detections_timeline_get_response import RecordingFaceDetectionsTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording face detections
        api_response = await api_instance.get_recording_face_detections_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)
        print("The response of CloudClientApi->get_recording_face_detections_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_face_detections_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**RecordingFaceDetectionsTimelineGetResponse**](RecordingFaceDetectionsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of face detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_files**
> RecordingFilesGetResponse get_recording_files(workspace_id, recording_id)

List recording files

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_files_get_response import RecordingFilesGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # List recording files
        api_response = await api_instance.get_recording_files(workspace_id, recording_id)
        print("The response of CloudClientApi->get_recording_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

[**RecordingFilesGetResponse**](RecordingFilesGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of a recording&#39;s files |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_fixations**
> RecordingFixationsGetResponse get_recording_fixations(workspace_id, recording_id, start=start, end=end, source=source)

Recording fixations

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_fixations_get_response import RecordingFixationsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    source = 'source_example' # str | source of the fixations (optional)

    try:
        # Recording fixations
        api_response = await api_instance.get_recording_fixations(workspace_id, recording_id, start=start, end=end, source=source)
        print("The response of CloudClientApi->get_recording_fixations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_fixations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **source** | **str**| source of the fixations | [optional] 

### Return type

[**RecordingFixationsGetResponse**](RecordingFixationsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording fixations |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_fixations_timeline**
> RecordingFixationsTimelineGetResponse get_recording_fixations_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)

Recording fixations timeline

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_fixations_timeline_get_response import RecordingFixationsTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording fixations timeline
        api_response = await api_instance.get_recording_fixations_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)
        print("The response of CloudClientApi->get_recording_fixations_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_fixations_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**RecordingFixationsTimelineGetResponse**](RecordingFixationsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of fixations |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_gaze**
> RecordingGazeGetResponse get_recording_gaze(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)

temporary endpoint for player development

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_gaze_get_response import RecordingGazeGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    max_length = 3.4 # float |  (optional)

    try:
        # temporary endpoint for player development
        api_response = await api_instance.get_recording_gaze(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)
        print("The response of CloudClientApi->get_recording_gaze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_gaze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **max_length** | **float**|  | [optional] 

### Return type

[**RecordingGazeGetResponse**](RecordingGazeGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of gaze points |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_scanpath**
> RecordingScanpathGetResponse get_recording_scanpath(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)

Get list of fixation scanpath points per world frame

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_scanpath_get_response import RecordingScanpathGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    max_length = 3.4 # float |  (optional)

    try:
        # Get list of fixation scanpath points per world frame
        api_response = await api_instance.get_recording_scanpath(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)
        print("The response of CloudClientApi->get_recording_scanpath:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_scanpath: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **max_length** | **float**|  | [optional] 

### Return type

[**RecordingScanpathGetResponse**](RecordingScanpathGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of fixation scanpath points |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_scene_camera_intrinsics**
> RecordingSceneCameraIntrinsicsGetResponse get_recording_scene_camera_intrinsics(workspace_id, recording_id, format)

Get Recording's Scene Camera Intrinsics

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_scene_camera_intrinsics_get_response import RecordingSceneCameraIntrinsicsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 

    try:
        # Get Recording's Scene Camera Intrinsics
        api_response = await api_instance.get_recording_scene_camera_intrinsics(workspace_id, recording_id, format)
        print("The response of CloudClientApi->get_recording_scene_camera_intrinsics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recording_scene_camera_intrinsics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 

### Return type

[**RecordingSceneCameraIntrinsicsGetResponse**](RecordingSceneCameraIntrinsicsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scene Camera Intrinsics of the specified recording |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recordings**
> RecordingsGetResponse get_recordings(workspace_id, trashed=trashed)

List all recordings

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recordings_get_response import RecordingsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    trashed = False # bool |  (optional) (default to False)

    try:
        # List all recordings
        api_response = await api_instance.get_recordings(workspace_id, trashed=trashed)
        print("The response of CloudClientApi->get_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **trashed** | **bool**|  | [optional] [default to False]

### Return type

[**RecordingsGetResponse**](RecordingsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recordings |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recordings_events_resource**
> get_recordings_events_resource(workspace_id)



### Example


```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)


# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        await api_instance.get_recordings_events_resource(workspace_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_recordings_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_render**
> RenderGetResponse get_render(workspace_id, render_definition_id)

Get a render enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.render_get_response import RenderGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    render_definition_id = 'render_definition_id_example' # str | 

    try:
        # Get a render enrichment
        api_response = await api_instance.get_render(workspace_id, render_definition_id)
        print("The response of CloudClientApi->get_render:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_render: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **render_definition_id** | **str**|  | 

### Return type

[**RenderGetResponse**](RenderGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A render definition |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_image_mapper_enrichment**
> StaticImageMapperEnrichmentGetResponse get_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)

Get a static image mapper enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichment_get_response import StaticImageMapperEnrichmentGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    static_enrichment_id = 'static_enrichment_id_example' # str | 

    try:
        # Get a static image mapper enrichment
        api_response = await api_instance.get_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)
        print("The response of CloudClientApi->get_static_image_mapper_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **static_enrichment_id** | **str**|  | 

### Return type

[**StaticImageMapperEnrichmentGetResponse**](StaticImageMapperEnrichmentGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A static image mapper enrichment |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Static image mapper enrichment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_image_mapper_enrichments**
> StaticImageMapperEnrichmentsGetResponse get_static_image_mapper_enrichments(workspace_id, project_id)

List all static image mapper enrichments of a project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichments_get_response import StaticImageMapperEnrichmentsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # List all static image mapper enrichments of a project
        api_response = await api_instance.get_static_image_mapper_enrichments(workspace_id, project_id)
        print("The response of CloudClientApi->get_static_image_mapper_enrichments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_static_image_mapper_enrichments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**StaticImageMapperEnrichmentsGetResponse**](StaticImageMapperEnrichmentsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of static image mapper enrichments of a project |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_image_mapper_enrichments_recording_fixations**
> StaticImageMapperEnrichmentsRecordingFixationsGetResponse get_static_image_mapper_enrichments_recording_fixations(workspace_id, project_id, enrichment_id, recording_id)

List all the fixations of a recording's static image mapper enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichments_recording_fixations_get_response import StaticImageMapperEnrichmentsRecordingFixationsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 

    try:
        # List all the fixations of a recording's static image mapper enrichments
        api_response = await api_instance.get_static_image_mapper_enrichments_recording_fixations(workspace_id, project_id, enrichment_id, recording_id)
        print("The response of CloudClientApi->get_static_image_mapper_enrichments_recording_fixations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_static_image_mapper_enrichments_recording_fixations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 

### Return type

[**StaticImageMapperEnrichmentsRecordingFixationsGetResponse**](StaticImageMapperEnrichmentsRecordingFixationsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fixations details along with total and mapped fixations count |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment or Recording or fixations.json or event section is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface**
> SurfaceGetResponse get_surface(workspace_id, surface_id)

Return surface definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_get_response import SurfaceGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 

    try:
        # Return surface definition
        api_response = await api_instance.get_surface(workspace_id, surface_id)
        print("The response of CloudClientApi->get_surface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_surface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 

### Return type

[**SurfaceGetResponse**](SurfaceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Surface definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface_corners**
> SurfaceCornersGetResponse get_surface_corners(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect, distorted=distorted)

get surface locations for surface enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_corners_get_response import SurfaceCornersGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | 
    end = 3.4 # float |  (optional)
    detect = 0 # int |  (optional) (default to 0)
    distorted = False # bool |  (optional) (default to False)

    try:
        # get surface locations for surface enrichment
        api_response = await api_instance.get_surface_corners(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect, distorted=distorted)
        print("The response of CloudClientApi->get_surface_corners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_surface_corners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **start** | **float**|  | 
 **end** | **float**|  | [optional] 
 **detect** | **int**|  | [optional] [default to 0]
 **distorted** | **bool**|  | [optional] [default to False]

### Return type

[**SurfaceCornersGetResponse**](SurfaceCornersGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of surface locations |  -  |
**400** | Enrichment doesn&#39;t belong to surface id |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Surface definition not found |  -  |
**405** | Project enrichment dosn&#39;t support surfaces |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface_detections_timeline**
> SurfaceDetectionsTimelineGetResponse get_surface_detections_timeline(workspace_id, surface_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)

Recording surface detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_detections_timeline_get_response import SurfaceDetectionsTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    recording_id2 = 'recording_id_example' # str | recording id
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording surface detections
        api_response = await api_instance.get_surface_detections_timeline(workspace_id, surface_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)
        print("The response of CloudClientApi->get_surface_detections_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_surface_detections_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **recording_id2** | **str**| recording id | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**SurfaceDetectionsTimelineGetResponse**](SurfaceDetectionsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of surface detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface_gaze_on_aoi**
> SurfaceGazeOnAoiGetResponse get_surface_gaze_on_aoi(workspace_id, surface_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)

get gaze on aoi data for markerless enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_gaze_on_aoi_get_response import SurfaceGazeOnAoiGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    project_id = 'project_id_example' # str |  (optional)
    enrichment_id = 'enrichment_id_example' # str |  (optional)
    recording_id = 'recording_id_example' # str |  (optional)
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)

    try:
        # get gaze on aoi data for markerless enrichment
        api_response = await api_instance.get_surface_gaze_on_aoi(workspace_id, surface_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)
        print("The response of CloudClientApi->get_surface_gaze_on_aoi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_surface_gaze_on_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **project_id** | **str**|  | [optional] 
 **enrichment_id** | **str**|  | [optional] 
 **recording_id** | **str**|  | [optional] 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 

### Return type

[**SurfaceGazeOnAoiGetResponse**](SurfaceGazeOnAoiGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of gaze in aoi coordinates with time ranges |  -  |
**400** | Enrichment doesn&#39;t belong to markerless id |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Markerless definition not found |  -  |
**405** | Enrichment does not support markerless |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> TemplateGetResponse get_template(workspace_id, template_id)

Returns a template with {template_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.template_get_response import TemplateGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    template_id = 'template_id_example' # str | 

    try:
        # Returns a template with {template_id}
        api_response = await api_instance.get_template(workspace_id, template_id)
        print("The response of CloudClientApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **template_id** | **str**|  | 

### Return type

[**TemplateGetResponse**](TemplateGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single template |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> TemplatesGetResponse get_templates(workspace_id)

List all templates

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.templates_get_response import TemplatesGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List all templates
        api_response = await api_instance.get_templates(workspace_id)
        print("The response of CloudClientApi->get_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**TemplatesGetResponse**](TemplatesGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of templates |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> TokenGetResponse get_token(token_id)

Get an access token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.token_get_response import TokenGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    token_id = 'token_id_example' # str | 

    try:
        # Get an access token
        api_response = await api_instance.get_token(token_id)
        print("The response of CloudClientApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 

### Return type

[**TokenGetResponse**](TokenGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens**
> TokensGetResponse get_tokens()

Get all access tokens

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.tokens_get_response import TokensGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)

    try:
        # Get all access tokens
        api_response = await api_instance.get_tokens()
        print("The response of CloudClientApi->get_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokensGetResponse**](TokensGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visualization_config**
> VisualizationConfigGetResponse get_visualization_config(workspace_id, project_id, visualization_config_id)

Get a visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_get_response import VisualizationConfigGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    visualization_config_id = 'visualization_config_id_example' # str | 

    try:
        # Get a visualization config
        api_response = await api_instance.get_visualization_config(workspace_id, project_id, visualization_config_id)
        print("The response of CloudClientApi->get_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **visualization_config_id** | **str**|  | 

### Return type

[**VisualizationConfigGetResponse**](VisualizationConfigGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A visualization config |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Visualization config not found |  -  |
**410** | Visualization config deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visualization_configs**
> VisualizationConfigsGetResponse get_visualization_configs(workspace_id, project_id)

List project's visualization configs

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_configs_get_response import VisualizationConfigsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # List project's visualization configs
        api_response = await api_instance.get_visualization_configs(workspace_id, project_id)
        print("The response of CloudClientApi->get_visualization_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_visualization_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**VisualizationConfigsGetResponse**](VisualizationConfigsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of project&#39;s visualization configs |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wearer**
> WearerGetResponse get_wearer(workspace_id, wearer_id)

Returns a wearer with {wearer_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.wearer_get_response import WearerGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    wearer_id = 'wearer_id_example' # str | 

    try:
        # Returns a wearer with {wearer_id}
        api_response = await api_instance.get_wearer(workspace_id, wearer_id)
        print("The response of CloudClientApi->get_wearer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_wearer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **wearer_id** | **str**|  | 

### Return type

[**WearerGetResponse**](WearerGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single wearer |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Wearer doesn&#39;t exist |  -  |
**410** | Wearer was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wearers**
> WearersGetResponse get_wearers(workspace_id)

List all wearers

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.wearers_get_response import WearersGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List all wearers
        api_response = await api_instance.get_wearers(workspace_id)
        print("The response of CloudClientApi->get_wearers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_wearers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**WearersGetResponse**](WearersGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of wearers |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> WorkspaceGetResponse get_workspace(workspace_id)

Returns the workspace with {workspace_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_get_response import WorkspaceGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # Returns the workspace with {workspace_id}
        api_response = await api_instance.get_workspace(workspace_id)
        print("The response of CloudClientApi->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**WorkspaceGetResponse**](WorkspaceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single workspace |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Workspace doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_invitation**
> WorkspaceInvitationGetResponse get_workspace_invitation(token)

get workspace inviation for token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_invitation_get_response import WorkspaceInvitationGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    token = 'token_example' # str | 

    try:
        # get workspace inviation for token
        api_response = await api_instance.get_workspace_invitation(token)
        print("The response of CloudClientApi->get_workspace_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_workspace_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**WorkspaceInvitationGetResponse**](WorkspaceInvitationGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace invitation |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_invitation_0**
> WorkspaceInvitationGetResponse get_workspace_invitation_0(workspace_id, token)

Get workspace invitation for token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_invitation_get_response import WorkspaceInvitationGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    token = 'token_example' # str | 

    try:
        # Get workspace invitation for token
        api_response = await api_instance.get_workspace_invitation_0(workspace_id, token)
        print("The response of CloudClientApi->get_workspace_invitation_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_workspace_invitation_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **token** | **str**|  | 

### Return type

[**WorkspaceInvitationGetResponse**](WorkspaceInvitationGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace invitation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_invitations**
> WorkspaceInvitationsGetResponse get_workspace_invitations()

List all workspace inviations for current user

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_invitations_get_response import WorkspaceInvitationsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)

    try:
        # List all workspace inviations for current user
        api_response = await api_instance.get_workspace_invitations()
        print("The response of CloudClientApi->get_workspace_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_workspace_invitations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceInvitationsGetResponse**](WorkspaceInvitationsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace invitations |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_member**
> WorkspaceMemberGetResponse get_workspace_member(workspace_id, user_id)

Get workspace member

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_member_get_response import WorkspaceMemberGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    user_id = 'user_id_example' # str | 

    try:
        # Get workspace member
        api_response = await api_instance.get_workspace_member(workspace_id, user_id)
        print("The response of CloudClientApi->get_workspace_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_workspace_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **user_id** | **str**|  | 

### Return type

[**WorkspaceMemberGetResponse**](WorkspaceMemberGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace member |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Workspace member not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_members**
> WorkspaceMembersGetResponse get_workspace_members(workspace_id)

List all members of workspace {workspace_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_members_get_response import WorkspaceMembersGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List all members of workspace {workspace_id}
        api_response = await api_instance.get_workspace_members(workspace_id)
        print("The response of CloudClientApi->get_workspace_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_workspace_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**WorkspaceMembersGetResponse**](WorkspaceMembersGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace members |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Workspace member not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**
> WorkspacesGetResponse get_workspaces()

List all workspaces for a user

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspaces_get_response import WorkspacesGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)

    try:
        # List all workspaces for a user
        api_response = await api_instance.get_workspaces()
        print("The response of CloudClientApi->get_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->get_workspaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspacesGetResponse**](WorkspacesGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of workspaces |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_markerless**
> InitializeMarkerlessResponse initialize_markerless(workspace_id, payload)

Create markerless definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.initialize_markerless_response import InitializeMarkerlessResponse
from pupilcloud.models.markerless_initialization import MarkerlessInitialization
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.MarkerlessInitialization() # MarkerlessInitialization | 

    try:
        # Create markerless definition
        api_response = await api_instance.initialize_markerless(workspace_id, payload)
        print("The response of CloudClientApi->initialize_markerless:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->initialize_markerless: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**MarkerlessInitialization**](MarkerlessInitialization.md)|  | 

### Return type

[**InitializeMarkerlessResponse**](InitializeMarkerlessResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_rendering**
> InitializeRenderingResponse initialize_rendering(workspace_id, payload)

Create world render definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.initialize_rendering_response import InitializeRenderingResponse
from pupilcloud.models.world_render import WorldRender
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.WorldRender() # WorldRender | 

    try:
        # Create world render definition
        api_response = await api_instance.initialize_rendering(workspace_id, payload)
        print("The response of CloudClientApi->initialize_rendering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->initialize_rendering: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**WorldRender**](WorldRender.md)|  | 

### Return type

[**InitializeRenderingResponse**](InitializeRenderingResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created render definition |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_invitations**
> WorkspaceInvitationsListResponse list_workspace_invitations(workspace_id)

List workspace invitations

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_invitations_list_response import WorkspaceInvitationsListResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List workspace invitations
        api_response = await api_instance.list_workspace_invitations(workspace_id)
        print("The response of CloudClientApi->list_workspace_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->list_workspace_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**WorkspaceInvitationsListResponse**](WorkspaceInvitationsListResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace invitations |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_aoi**
> AoiPatchResponse patch_aoi(workspace_id, project_id, enrichment_id, aoi_id, payload)

Update an aoi

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aoi_patch_request import AoiPatchRequest
from pupilcloud.models.aoi_patch_response import AoiPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    aoi_id = 'aoi_id_example' # str | 
    payload = pupilcloud.AoiPatchRequest() # AoiPatchRequest | 

    try:
        # Update an aoi
        api_response = await api_instance.patch_aoi(workspace_id, project_id, enrichment_id, aoi_id, payload)
        print("The response of CloudClientApi->patch_aoi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **aoi_id** | **str**|  | 
 **payload** | [**AoiPatchRequest**](AoiPatchRequest.md)|  | 

### Return type

[**AoiPatchResponse**](AoiPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated aoi |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_filter**
> FilterPatchResponse patch_filter(workspace_id, filter_id, payload)

Update a filter

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.filter_patch_request import FilterPatchRequest
from pupilcloud.models.filter_patch_response import FilterPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    filter_id = 'filter_id_example' # str | 
    payload = pupilcloud.FilterPatchRequest() # FilterPatchRequest | 

    try:
        # Update a filter
        api_response = await api_instance.patch_filter(workspace_id, filter_id, payload)
        print("The response of CloudClientApi->patch_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **filter_id** | **str**|  | 
 **payload** | [**FilterPatchRequest**](FilterPatchRequest.md)|  | 

### Return type

[**FilterPatchResponse**](FilterPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated filter |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_label**
> LabelPatchResponse patch_label(workspace_id, label_id, payload)

Update a label

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.label_patch_request import LabelPatchRequest
from pupilcloud.models.label_patch_response import LabelPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    label_id = 'label_id_example' # str | 
    payload = pupilcloud.LabelPatchRequest() # LabelPatchRequest | 

    try:
        # Update a label
        api_response = await api_instance.patch_label(workspace_id, label_id, payload)
        print("The response of CloudClientApi->patch_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **label_id** | **str**|  | 
 **payload** | [**LabelPatchRequest**](LabelPatchRequest.md)|  | 

### Return type

[**LabelPatchResponse**](LabelPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated label |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_profile**
> ProfilePatchResponse patch_profile(payload)

Update user profile

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.profile_patch_request import ProfilePatchRequest
from pupilcloud.models.profile_patch_response import ProfilePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    payload = pupilcloud.ProfilePatchRequest() # ProfilePatchRequest | 

    try:
        # Update user profile
        api_response = await api_instance.patch_profile(payload)
        print("The response of CloudClientApi->patch_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ProfilePatchRequest**](ProfilePatchRequest.md)|  | 

### Return type

[**ProfilePatchResponse**](ProfilePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated profile |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_enrichment_resource**
> ProjectEnrichmentResourcePatchResponse patch_project_enrichment_resource(workspace_id, project_id, enrichment_id, payload)

Update a project enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_patch_request import ProjectEnrichmentPatchRequest
from pupilcloud.models.project_enrichment_resource_patch_response import ProjectEnrichmentResourcePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.ProjectEnrichmentPatchRequest() # ProjectEnrichmentPatchRequest | 

    try:
        # Update a project enrichment
        api_response = await api_instance.patch_project_enrichment_resource(workspace_id, project_id, enrichment_id, payload)
        print("The response of CloudClientApi->patch_project_enrichment_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_project_enrichment_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**ProjectEnrichmentPatchRequest**](ProjectEnrichmentPatchRequest.md)|  | 

### Return type

[**ProjectEnrichmentResourcePatchResponse**](ProjectEnrichmentResourcePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated project enrichment |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_recording_event_resource**
> ProjectRecordingEventResourcePatchResponse patch_project_recording_event_resource(workspace_id, project_id, recording_id, event_id, payload)

Update a project recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recording_event_patch_request import ProjectRecordingEventPatchRequest
from pupilcloud.models.project_recording_event_resource_patch_response import ProjectRecordingEventResourcePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 
    payload = pupilcloud.ProjectRecordingEventPatchRequest() # ProjectRecordingEventPatchRequest | 

    try:
        # Update a project recording event
        api_response = await api_instance.patch_project_recording_event_resource(workspace_id, project_id, recording_id, event_id, payload)
        print("The response of CloudClientApi->patch_project_recording_event_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_project_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 
 **payload** | [**ProjectRecordingEventPatchRequest**](ProjectRecordingEventPatchRequest.md)|  | 

### Return type

[**ProjectRecordingEventResourcePatchResponse**](ProjectRecordingEventResourcePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated event |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_resource**
> ProjectResourcePatchResponse patch_project_resource(workspace_id, project_id, payload)

Update a project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_patch_request import ProjectPatchRequest
from pupilcloud.models.project_resource_patch_response import ProjectResourcePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.ProjectPatchRequest() # ProjectPatchRequest | 

    try:
        # Update a project
        api_response = await api_instance.patch_project_resource(workspace_id, project_id, payload)
        print("The response of CloudClientApi->patch_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**ProjectPatchRequest**](ProjectPatchRequest.md)|  | 

### Return type

[**ProjectResourcePatchResponse**](ProjectResourcePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated project |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recording**
> RecordingPatchResponse patch_recording(workspace_id, recording_id, payload)

Update a recording

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_patch_request import RecordingPatchRequest
from pupilcloud.models.recording_patch_response import RecordingPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    payload = pupilcloud.RecordingPatchRequest() # RecordingPatchRequest | 

    try:
        # Update a recording
        api_response = await api_instance.patch_recording(workspace_id, recording_id, payload)
        print("The response of CloudClientApi->patch_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **payload** | [**RecordingPatchRequest**](RecordingPatchRequest.md)|  | 

### Return type

[**RecordingPatchResponse**](RecordingPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated recording |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recording_event_resource**
> RecordingEventResourcePatchResponse patch_recording_event_resource(workspace_id, recording_id, event_id, payload)

Update a recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_event_patch_request import RecordingEventPatchRequest
from pupilcloud.models.recording_event_resource_patch_response import RecordingEventResourcePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 
    payload = pupilcloud.RecordingEventPatchRequest() # RecordingEventPatchRequest | 

    try:
        # Update a recording event
        api_response = await api_instance.patch_recording_event_resource(workspace_id, recording_id, event_id, payload)
        print("The response of CloudClientApi->patch_recording_event_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 
 **payload** | [**RecordingEventPatchRequest**](RecordingEventPatchRequest.md)|  | 

### Return type

[**RecordingEventResourcePatchResponse**](RecordingEventResourcePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated event |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_render**
> RenderPatchResponse patch_render(workspace_id, render_definition_id, payload)

Update a render enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.render_patch_response import RenderPatchResponse
from pupilcloud.models.world_render import WorldRender
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    render_definition_id = 'render_definition_id_example' # str | 
    payload = pupilcloud.WorldRender() # WorldRender | 

    try:
        # Update a render enrichment
        api_response = await api_instance.patch_render(workspace_id, render_definition_id, payload)
        print("The response of CloudClientApi->patch_render:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_render: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **render_definition_id** | **str**|  | 
 **payload** | [**WorldRender**](WorldRender.md)|  | 

### Return type

[**RenderPatchResponse**](RenderPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated render definition |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Render definition not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_rotate_surface_orientation**
> patch_rotate_surface_orientation(workspace_id, surface_id, payload)

Change surface rotation

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.orientation_rotation import OrientationRotation
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    payload = pupilcloud.OrientationRotation() # OrientationRotation | 

    try:
        # Change surface rotation
        await api_instance.patch_rotate_surface_orientation(workspace_id, surface_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_rotate_surface_orientation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **payload** | [**OrientationRotation**](OrientationRotation.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Surface definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_static_image_mapper_enrichment**
> StaticImageMapperEnrichmentPatchResponse patch_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id, payload)

Update a static image mapper enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichment_patch_response import StaticImageMapperEnrichmentPatchResponse
from pupilcloud.models.static_image_mapper_patch_request import StaticImageMapperPatchRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    static_enrichment_id = 'static_enrichment_id_example' # str | 
    payload = pupilcloud.StaticImageMapperPatchRequest() # StaticImageMapperPatchRequest | 

    try:
        # Update a static image mapper enrichment
        api_response = await api_instance.patch_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id, payload)
        print("The response of CloudClientApi->patch_static_image_mapper_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **static_enrichment_id** | **str**|  | 
 **payload** | [**StaticImageMapperPatchRequest**](StaticImageMapperPatchRequest.md)|  | 

### Return type

[**StaticImageMapperEnrichmentPatchResponse**](StaticImageMapperEnrichmentPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated static image mapper enrichment |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Static image mapper enrichment not found |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_surface**
> SurfacePatchResponse patch_surface(workspace_id, surface_id, payload)

Update surface definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.patch_surface import PatchSurface
from pupilcloud.models.surface_patch_response import SurfacePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    payload = pupilcloud.PatchSurface() # PatchSurface | 

    try:
        # Update surface definition
        api_response = await api_instance.patch_surface(workspace_id, surface_id, payload)
        print("The response of CloudClientApi->patch_surface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_surface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **payload** | [**PatchSurface**](PatchSurface.md)|  | 

### Return type

[**SurfacePatchResponse**](SurfacePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Error updating surface |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Surface definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_template**
> TemplatePatchResponse patch_template(workspace_id, template_id, payload)

Update a template

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.template_patch_request import TemplatePatchRequest
from pupilcloud.models.template_patch_response import TemplatePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    template_id = 'template_id_example' # str | 
    payload = pupilcloud.TemplatePatchRequest() # TemplatePatchRequest | 

    try:
        # Update a template
        api_response = await api_instance.patch_template(workspace_id, template_id, payload)
        print("The response of CloudClientApi->patch_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **template_id** | **str**|  | 
 **payload** | [**TemplatePatchRequest**](TemplatePatchRequest.md)|  | 

### Return type

[**TemplatePatchResponse**](TemplatePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated template |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_visualization_config**
> VisualizationConfigPatchResponse patch_visualization_config(workspace_id, project_id, visualization_config_id, payload)

Update a visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_patch_request import VisualizationConfigPatchRequest
from pupilcloud.models.visualization_config_patch_response import VisualizationConfigPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    visualization_config_id = 'visualization_config_id_example' # str | 
    payload = pupilcloud.VisualizationConfigPatchRequest() # VisualizationConfigPatchRequest | 

    try:
        # Update a visualization config
        api_response = await api_instance.patch_visualization_config(workspace_id, project_id, visualization_config_id, payload)
        print("The response of CloudClientApi->patch_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **visualization_config_id** | **str**|  | 
 **payload** | [**VisualizationConfigPatchRequest**](VisualizationConfigPatchRequest.md)|  | 

### Return type

[**VisualizationConfigPatchResponse**](VisualizationConfigPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated visualization config |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Visualization config not found |  -  |
**410** | Visualization config deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_wearer**
> WearerPatchResponse patch_wearer(workspace_id, wearer_id, payload)

Update a wearer

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.wearer_patch_request import WearerPatchRequest
from pupilcloud.models.wearer_patch_response import WearerPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    wearer_id = 'wearer_id_example' # str | 
    payload = pupilcloud.WearerPatchRequest() # WearerPatchRequest | 

    try:
        # Update a wearer
        api_response = await api_instance.patch_wearer(workspace_id, wearer_id, payload)
        print("The response of CloudClientApi->patch_wearer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_wearer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **wearer_id** | **str**|  | 
 **payload** | [**WearerPatchRequest**](WearerPatchRequest.md)|  | 

### Return type

[**WearerPatchResponse**](WearerPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated wearer |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Wearer doesn&#39;t exist |  -  |
**409** | Invalid input |  -  |
**410** | Wearer was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_workspace_member**
> WorkspaceMemberPatchResponse patch_workspace_member(workspace_id, user_id, payload)

Patch members of workspace {workspace_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_member_patch_request import WorkspaceMemberPatchRequest
from pupilcloud.models.workspace_member_patch_response import WorkspaceMemberPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    user_id = 'user_id_example' # str | 
    payload = pupilcloud.WorkspaceMemberPatchRequest() # WorkspaceMemberPatchRequest | 

    try:
        # Patch members of workspace {workspace_id}
        api_response = await api_instance.patch_workspace_member(workspace_id, user_id, payload)
        print("The response of CloudClientApi->patch_workspace_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->patch_workspace_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **user_id** | **str**|  | 
 **payload** | [**WorkspaceMemberPatchRequest**](WorkspaceMemberPatchRequest.md)|  | 

### Return type

[**WorkspaceMemberPatchResponse**](WorkspaceMemberPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch workspace members |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Workspace member not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accept_invitation_resource**
> AcceptInvitationResourcePostResponse post_accept_invitation_resource(token)

Create workspace member based on invite token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.accept_invitation_resource_post_response import AcceptInvitationResourcePostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    token = 'token_example' # str | 

    try:
        # Create workspace member based on invite token
        api_response = await api_instance.post_accept_invitation_resource(token)
        print("The response of CloudClientApi->post_accept_invitation_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_accept_invitation_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**AcceptInvitationResourcePostResponse**](AcceptInvitationResourcePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace member |  -  |
**401** | Authentication is required |  -  |
**409** | Member already member of workspace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aoi**
> AoiPostResponse post_aoi(workspace_id, project_id, enrichment_id, payload)

Create a new aoi

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aoi_post_request import AoiPostRequest
from pupilcloud.models.aoi_post_response import AoiPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.AoiPostRequest() # AoiPostRequest | 

    try:
        # Create a new aoi
        api_response = await api_instance.post_aoi(workspace_id, project_id, enrichment_id, payload)
        print("The response of CloudClientApi->post_aoi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**AoiPostRequest**](AoiPostRequest.md)|  | 

### Return type

[**AoiPostResponse**](AoiPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created Aoi |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aoi_0**
> AoiPostResponse post_aoi_0(workspace_id, project_id, enrichment_id, aoi_id, payload)

Create a new aoi

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aoi_post_request import AoiPostRequest
from pupilcloud.models.aoi_post_response import AoiPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    aoi_id = 'aoi_id_example' # str | 
    payload = pupilcloud.AoiPostRequest() # AoiPostRequest | 

    try:
        # Create a new aoi
        api_response = await api_instance.post_aoi_0(workspace_id, project_id, enrichment_id, aoi_id, payload)
        print("The response of CloudClientApi->post_aoi_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_aoi_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **aoi_id** | **str**|  | 
 **payload** | [**AoiPostRequest**](AoiPostRequest.md)|  | 

### Return type

[**AoiPostResponse**](AoiPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created aoi |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aoi_1**
> AoiPostResponse post_aoi_1(workspace_id, project_id, enrichment_id, payload)

Create a new aoi

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.aoi_post_request import AoiPostRequest
from pupilcloud.models.aoi_post_response import AoiPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.AoiPostRequest() # AoiPostRequest | 

    try:
        # Create a new aoi
        api_response = await api_instance.post_aoi_1(workspace_id, project_id, enrichment_id, payload)
        print("The response of CloudClientApi->post_aoi_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_aoi_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**AoiPostRequest**](AoiPostRequest.md)|  | 

### Return type

[**AoiPostResponse**](AoiPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created Aoi |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_distorted_surface_location**
> DistortedSurfaceLocationPostResponse post_distorted_surface_location(workspace_id, surface_id, payload)

Set distorted surface corner locations

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.distorted_surface_location_post_response import DistortedSurfaceLocationPostResponse
from pupilcloud.models.set_distorted_surface_request import SetDistortedSurfaceRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    payload = pupilcloud.SetDistortedSurfaceRequest() # SetDistortedSurfaceRequest | 

    try:
        # Set distorted surface corner locations
        api_response = await api_instance.post_distorted_surface_location(workspace_id, surface_id, payload)
        print("The response of CloudClientApi->post_distorted_surface_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_distorted_surface_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **payload** | [**SetDistortedSurfaceRequest**](SetDistortedSurfaceRequest.md)|  | 

### Return type

[**DistortedSurfaceLocationPostResponse**](DistortedSurfaceLocationPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Surface corner coordinates |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Surface definition not found |  -  |
**501** | No markers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_download_heatmap**
> bytearray post_download_heatmap(workspace_id, payload)

download zip file with heatmaps

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.generate_heatmap import GenerateHeatmap
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.GenerateHeatmap() # GenerateHeatmap | 

    try:
        # download zip file with heatmaps
        api_response = await api_instance.post_download_heatmap(workspace_id, payload)
        print("The response of CloudClientApi->post_download_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_download_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**GenerateHeatmap**](GenerateHeatmap.md)|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_filters**
> FiltersPostResponse post_filters(workspace_id, payload)

Create a new filter

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.filter_post_request import FilterPostRequest
from pupilcloud.models.filters_post_response import FiltersPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.FilterPostRequest() # FilterPostRequest | 

    try:
        # Create a new filter
        api_response = await api_instance.post_filters(workspace_id, payload)
        print("The response of CloudClientApi->post_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**FilterPostRequest**](FilterPostRequest.md)|  | 

### Return type

[**FiltersPostResponse**](FiltersPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created filter |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_heatmap**
> bytearray post_heatmap(workspace_id, payload)

get heatmap image or json data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.generate_heatmap import GenerateHeatmap
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.GenerateHeatmap() # GenerateHeatmap | 

    try:
        # get heatmap image or json data
        api_response = await api_instance.post_heatmap(workspace_id, payload)
        print("The response of CloudClientApi->post_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**GenerateHeatmap**](GenerateHeatmap.md)|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_label**
> LabelPostResponse post_label(workspace_id, payload)

Create a new label

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.label_post_request import LabelPostRequest
from pupilcloud.models.label_post_response import LabelPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.LabelPostRequest() # LabelPostRequest | 

    try:
        # Create a new label
        api_response = await api_instance.post_label(workspace_id, payload)
        print("The response of CloudClientApi->post_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**LabelPostRequest**](LabelPostRequest.md)|  | 

### Return type

[**LabelPostResponse**](LabelPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created label |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_label_0**
> LabelPostResponse post_label_0(workspace_id, label_id, payload)

Create a new label

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.label_post_request import LabelPostRequest
from pupilcloud.models.label_post_response import LabelPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    label_id = 'label_id_example' # str | 
    payload = pupilcloud.LabelPostRequest() # LabelPostRequest | 

    try:
        # Create a new label
        api_response = await api_instance.post_label_0(workspace_id, label_id, payload)
        print("The response of CloudClientApi->post_label_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_label_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **label_id** | **str**|  | 
 **payload** | [**LabelPostRequest**](LabelPostRequest.md)|  | 

### Return type

[**LabelPostResponse**](LabelPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created label |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_login**
> LoginPostResponse post_login(payload)

Login the user and return a new session cookie

### Example


```python
import pupilcloud
from pupilcloud.models.login_post_response import LoginPostResponse
from pupilcloud.models.login_request import LoginRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)


# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    payload = pupilcloud.LoginRequest() # LoginRequest | 

    try:
        # Login the user and return a new session cookie
        api_response = await api_instance.post_login(payload)
        print("The response of CloudClientApi->post_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**LoginPostResponse**](LoginPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login success |  -  |
**400** | Invalid input |  -  |
**401** | Invalid token |  -  |
**403** | Token expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_logout**
> LogoutPostResponse post_logout()

Logout the current user

### Example


```python
import pupilcloud
from pupilcloud.models.logout_post_response import LogoutPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)


# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)

    try:
        # Logout the current user
        api_response = await api_instance.post_logout()
        print("The response of CloudClientApi->post_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LogoutPostResponse**](LogoutPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_download_resource**
> post_project_download_resource(workspace_id, project_id, payload)

Download project data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_download_request import ProjectDownloadRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.ProjectDownloadRequest() # ProjectDownloadRequest | 

    try:
        # Download project data
        await api_instance.post_project_download_resource(workspace_id, project_id, payload)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_project_download_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**ProjectDownloadRequest**](ProjectDownloadRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment**
> ProjectEnrichmentPostResponse post_project_enrichment(workspace_id, project_id, payload)

Create a new project enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_post_request import ProjectEnrichmentPostRequest
from pupilcloud.models.project_enrichment_post_response import ProjectEnrichmentPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.ProjectEnrichmentPostRequest() # ProjectEnrichmentPostRequest | 

    try:
        # Create a new project enrichment
        api_response = await api_instance.post_project_enrichment(workspace_id, project_id, payload)
        print("The response of CloudClientApi->post_project_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_project_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**ProjectEnrichmentPostRequest**](ProjectEnrichmentPostRequest.md)|  | 

### Return type

[**ProjectEnrichmentPostResponse**](ProjectEnrichmentPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created project enrichment |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment_cancel_resource**
> post_project_enrichment_cancel_resource(workspace_id, project_id, enrichment_id)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        await api_instance.post_project_enrichment_cancel_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_project_enrichment_cancel_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment_compute_resource**
> post_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        await api_instance.post_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_project_enrichment_compute_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**405** | Enrichment not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment_export_resource**
> bytearray post_project_enrichment_export_resource(workspace_id, project_id, enrichment_id, payload)

Export an enrichment data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_export import ProjectEnrichmentExport
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.ProjectEnrichmentExport() # ProjectEnrichmentExport | 

    try:
        # Export an enrichment data
        api_response = await api_instance.post_project_enrichment_export_resource(workspace_id, project_id, enrichment_id, payload)
        print("The response of CloudClientApi->post_project_enrichment_export_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_project_enrichment_export_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**ProjectEnrichmentExport**](ProjectEnrichmentExport.md)|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | ProjectEnrichment doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_recording_events_resource**
> ProjectRecordingEventsResourcePostResponse post_project_recording_events_resource(workspace_id, project_id, recording_id, payload)

Create a new project recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recording_event_post_request import ProjectRecordingEventPostRequest
from pupilcloud.models.project_recording_events_resource_post_response import ProjectRecordingEventsResourcePostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    payload = pupilcloud.ProjectRecordingEventPostRequest() # ProjectRecordingEventPostRequest | 

    try:
        # Create a new project recording event
        api_response = await api_instance.post_project_recording_events_resource(workspace_id, project_id, recording_id, payload)
        print("The response of CloudClientApi->post_project_recording_events_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_project_recording_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **payload** | [**ProjectRecordingEventPostRequest**](ProjectRecordingEventPostRequest.md)|  | 

### Return type

[**ProjectRecordingEventsResourcePostResponse**](ProjectRecordingEventsResourcePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created project recording event |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_projects_resource**
> ProjectsResourcePostResponse post_projects_resource(workspace_id, payload)

Create a new project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_post_request import ProjectPostRequest
from pupilcloud.models.projects_resource_post_response import ProjectsResourcePostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.ProjectPostRequest() # ProjectPostRequest | 

    try:
        # Create a new project
        api_response = await api_instance.post_projects_resource(workspace_id, payload)
        print("The response of CloudClientApi->post_projects_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_projects_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**ProjectPostRequest**](ProjectPostRequest.md)|  | 

### Return type

[**ProjectsResourcePostResponse**](ProjectsResourcePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created project |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_recording_event**
> RecordingEventPostResponse post_recording_event(workspace_id, recording_id, payload)

Create a new recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_event_post_request import RecordingEventPostRequest
from pupilcloud.models.recording_event_post_response import RecordingEventPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    payload = pupilcloud.RecordingEventPostRequest() # RecordingEventPostRequest | 

    try:
        # Create a new recording event
        api_response = await api_instance.post_recording_event(workspace_id, recording_id, payload)
        print("The response of CloudClientApi->post_recording_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_recording_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **payload** | [**RecordingEventPostRequest**](RecordingEventPostRequest.md)|  | 

### Return type

[**RecordingEventPostResponse**](RecordingEventPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created recording event |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_static_image_mapper_enrichment**
> StaticImageMapperEnrichmentPostResponse post_static_image_mapper_enrichment(workspace_id, project_id, payload)

Create a new static image mapper enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichment_post_response import StaticImageMapperEnrichmentPostResponse
from pupilcloud.models.static_image_mapper_post_request import StaticImageMapperPostRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.StaticImageMapperPostRequest() # StaticImageMapperPostRequest | 

    try:
        # Create a new static image mapper enrichment
        api_response = await api_instance.post_static_image_mapper_enrichment(workspace_id, project_id, payload)
        print("The response of CloudClientApi->post_static_image_mapper_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**StaticImageMapperPostRequest**](StaticImageMapperPostRequest.md)|  | 

### Return type

[**StaticImageMapperEnrichmentPostResponse**](StaticImageMapperEnrichmentPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created static image mapper enrichment |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_surface**
> SurfacePostResponse post_surface(workspace_id, payload)

Create a new surface definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_initialization import SurfaceInitialization
from pupilcloud.models.surface_post_response import SurfacePostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.SurfaceInitialization() # SurfaceInitialization | 

    try:
        # Create a new surface definition
        api_response = await api_instance.post_surface(workspace_id, payload)
        print("The response of CloudClientApi->post_surface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_surface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**SurfaceInitialization**](SurfaceInitialization.md)|  | 

### Return type

[**SurfacePostResponse**](SurfacePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_template**
> TemplatePostResponse post_template(workspace_id, payload)

Create a new template

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.template_post_request import TemplatePostRequest
from pupilcloud.models.template_post_response import TemplatePostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.TemplatePostRequest() # TemplatePostRequest | 

    try:
        # Create a new template
        api_response = await api_instance.post_template(workspace_id, payload)
        print("The response of CloudClientApi->post_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**TemplatePostRequest**](TemplatePostRequest.md)|  | 

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created template |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_token**
> TokenPostResponse post_token(payload)

Creates a new access token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.token_post_request import TokenPostRequest
from pupilcloud.models.token_post_response import TokenPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    payload = pupilcloud.TokenPostRequest() # TokenPostRequest | 

    try:
        # Creates a new access token
        api_response = await api_instance.post_token(payload)
        print("The response of CloudClientApi->post_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TokenPostRequest**](TokenPostRequest.md)|  | 

### Return type

[**TokenPostResponse**](TokenPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_unregister**
> post_unregister()

Unregisters the currently logged in user

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)

    try:
        # Unregisters the currently logged in user
        await api_instance.post_unregister()
    except Exception as e:
        print("Exception when calling CloudClientApi->post_unregister: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unregistered successully |  -  |
**401** | Unauthorized / cookie expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_visualization_config**
> VisualizationConfigPostResponse post_visualization_config(workspace_id, project_id, payload)

Create a new visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_post_request import VisualizationConfigPostRequest
from pupilcloud.models.visualization_config_post_response import VisualizationConfigPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.VisualizationConfigPostRequest() # VisualizationConfigPostRequest | 

    try:
        # Create a new visualization config
        api_response = await api_instance.post_visualization_config(workspace_id, project_id, payload)
        print("The response of CloudClientApi->post_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**VisualizationConfigPostRequest**](VisualizationConfigPostRequest.md)|  | 

### Return type

[**VisualizationConfigPostResponse**](VisualizationConfigPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created visualization config |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wearer**
> WearerPostResponse post_wearer(workspace_id, payload)

Create a new wearer

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.wearer_post_request import WearerPostRequest
from pupilcloud.models.wearer_post_response import WearerPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.WearerPostRequest() # WearerPostRequest | 

    try:
        # Create a new wearer
        api_response = await api_instance.post_wearer(workspace_id, payload)
        print("The response of CloudClientApi->post_wearer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_wearer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**WearerPostRequest**](WearerPostRequest.md)|  | 

### Return type

[**WearerPostResponse**](WearerPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created wearer |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace**
> WorkspacePostResponse post_workspace(payload)

Create a new workspace

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_post_request import WorkspacePostRequest
from pupilcloud.models.workspace_post_response import WorkspacePostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    payload = pupilcloud.WorkspacePostRequest() # WorkspacePostRequest | 

    try:
        # Create a new workspace
        api_response = await api_instance.post_workspace(payload)
        print("The response of CloudClientApi->post_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**WorkspacePostRequest**](WorkspacePostRequest.md)|  | 

### Return type

[**WorkspacePostResponse**](WorkspacePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created a workspace |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace_members_resource**
> WorkspaceMembersResourcePostResponse post_workspace_members_resource(workspace_id, payload)

Add workspace member

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_member_post_request import WorkspaceMemberPostRequest
from pupilcloud.models.workspace_members_resource_post_response import WorkspaceMembersResourcePostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.WorkspaceMemberPostRequest() # WorkspaceMemberPostRequest | 

    try:
        # Add workspace member
        api_response = await api_instance.post_workspace_members_resource(workspace_id, payload)
        print("The response of CloudClientApi->post_workspace_members_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->post_workspace_members_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**WorkspaceMemberPostRequest**](WorkspaceMemberPostRequest.md)|  | 

### Return type

[**WorkspaceMembersResourcePostResponse**](WorkspaceMembersResourcePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Workspace doesn&#39;t exist |  -  |
**409** | Member already member of workspace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_enrichments_export**
> bytearray project_enrichments_export(workspace_id, project_id, enrichment_id, recording_ids=recording_ids)

Export an enrichment data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_ids = ['recording_ids_example'] # List[str] | Recordings UUIDs for which data is to be exported (optional)

    try:
        # Export an enrichment data
        api_response = await api_instance.project_enrichments_export(workspace_id, project_id, enrichment_id, recording_ids=recording_ids)
        print("The response of CloudClientApi->project_enrichments_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->project_enrichments_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_ids** | [**List[str]**](str.md)| Recordings UUIDs for which data is to be exported | [optional] 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | ProjectEnrichment doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_static_image_mapper_enrichments_recording_fixation**
> StaticImageMapperEnrichmentsRecordingFixationPutResponse put_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id, payload)

Insert or update coordinates of a particular fixation of recording's

static image mapper enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichments_recording_fixation_put_response import StaticImageMapperEnrichmentsRecordingFixationPutResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    fixation_id = 56 # int | 
    payload = None # object | 

    try:
        # Insert or update coordinates of a particular fixation of recording's
        api_response = await api_instance.put_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id, payload)
        print("The response of CloudClientApi->put_static_image_mapper_enrichments_recording_fixation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->put_static_image_mapper_enrichments_recording_fixation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **fixation_id** | **int**|  | 
 **payload** | **object**|  | 

### Return type

[**StaticImageMapperEnrichmentsRecordingFixationPutResponse**](StaticImageMapperEnrichmentsRecordingFixationPutResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Particular fixation data of that recording |  -  |
**201** | Updated fixation data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Enrichment or Recording or fixations.json or event section is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_markerless**
> scan_markerless(workspace_id, markerless_id)

Scan markerless

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 

    try:
        # Scan markerless
        await api_instance.scan_markerless(workspace_id, markerless_id)
    except Exception as e:
        print("Exception when calling CloudClientApi->scan_markerless: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Markerless definition not found |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> WorkspaceUpdateResponse update_workspace(workspace_id, payload)

Update a workspace

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_patch_request import WorkspacePatchRequest
from pupilcloud.models.workspace_update_response import WorkspaceUpdateResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.CloudClientApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.WorkspacePatchRequest() # WorkspacePatchRequest | 

    try:
        # Update a workspace
        api_response = await api_instance.update_workspace(workspace_id, payload)
        print("The response of CloudClientApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudClientApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**WorkspacePatchRequest**](WorkspacePatchRequest.md)|  | 

### Return type

[**WorkspaceUpdateResponse**](WorkspaceUpdateResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a workspace |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

