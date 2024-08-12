# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pupilcloud.cloud_client_api import CloudClientApi


class TestCloudClientApi(unittest.TestCase):
    """CloudClientApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CloudClientApi()

    def tearDown(self) -> None:
        pass

    def test_clear_static_image_mapper_enrichments_recording_fixation(self) -> None:
        """Test case for clear_static_image_mapper_enrichments_recording_fixation

        Clear or resets all the mapped fixation of recording's
        """
        pass

    def test_create_recording_event(self) -> None:
        """Test case for create_recording_event

        Create recording event
        """
        pass

    def test_create_workspace_invitation(self) -> None:
        """Test case for create_workspace_invitation

        Create a workspace invitation
        """
        pass

    def test_delete_aoi(self) -> None:
        """Test case for delete_aoi

        Delete an aoi
        """
        pass

    def test_delete_aois(self) -> None:
        """Test case for delete_aois

        Delete multiple aois
        """
        pass

    def test_delete_aois_0(self) -> None:
        """Test case for delete_aois_0

        Delete multiple aois
        """
        pass

    def test_delete_filter(self) -> None:
        """Test case for delete_filter

        Delete a filter
        """
        pass

    def test_delete_filters(self) -> None:
        """Test case for delete_filters

        Delete multiple filters
        """
        pass

    def test_delete_label(self) -> None:
        """Test case for delete_label

        Delete a label
        """
        pass

    def test_delete_labels(self) -> None:
        """Test case for delete_labels

        Delete multiple labels
        """
        pass

    def test_delete_project_enrichment_resource(self) -> None:
        """Test case for delete_project_enrichment_resource

        Delete a project enrichment
        """
        pass

    def test_delete_project_recording_event_resource(self) -> None:
        """Test case for delete_project_recording_event_resource

        Delete a project recording event
        """
        pass

    def test_delete_project_resource(self) -> None:
        """Test case for delete_project_resource

        Delete a project
        """
        pass

    def test_delete_projects_resource(self) -> None:
        """Test case for delete_projects_resource

        Delete multiple projects
        """
        pass

    def test_delete_recording(self) -> None:
        """Test case for delete_recording

        Delete a recording
        """
        pass

    def test_delete_recording_event_resource(self) -> None:
        """Test case for delete_recording_event_resource

        Delete a recording event
        """
        pass

    def test_delete_recordings(self) -> None:
        """Test case for delete_recordings

        Delete multiple recordings
        """
        pass

    def test_delete_static_image_mapper_enrichments_recording_fixation(self) -> None:
        """Test case for delete_static_image_mapper_enrichments_recording_fixation

        Deletes coordinates of a particular fixation of recording's
        """
        pass

    def test_delete_template(self) -> None:
        """Test case for delete_template

        Delete a template
        """
        pass

    def test_delete_templates(self) -> None:
        """Test case for delete_templates

        Delete multiple templates
        """
        pass

    def test_delete_token(self) -> None:
        """Test case for delete_token

        Delete an access token
        """
        pass

    def test_delete_visualization_config(self) -> None:
        """Test case for delete_visualization_config

        Delete a visualization config
        """
        pass

    def test_delete_wearer(self) -> None:
        """Test case for delete_wearer

        Delete a wearer
        """
        pass

    def test_delete_wearers(self) -> None:
        """Test case for delete_wearers

        Delete multiple wearers
        """
        pass

    def test_delete_workspace(self) -> None:
        """Test case for delete_workspace

        Delete a workspace
        """
        pass

    def test_delete_workspace_invitation(self) -> None:
        """Test case for delete_workspace_invitation

        Delete a workspace invitation
        """
        pass

    def test_delete_workspace_invitation_0(self) -> None:
        """Test case for delete_workspace_invitation_0

        Delete a workspace invitation
        """
        pass

    def test_delete_workspace_member(self) -> None:
        """Test case for delete_workspace_member

        Delete a workspace member from a workspace
        """
        pass

    def test_download_raw_data_export_zip(self) -> None:
        """Test case for download_raw_data_export_zip

        """
        pass

    def test_download_recording_file(self) -> None:
        """Test case for download_recording_file

        Download a recording's file
        """
        pass

    def test_download_recording_zip(self) -> None:
        """Test case for download_recording_zip

        Download recording files as a zip file
        """
        pass

    def test_download_recordings_zip(self) -> None:
        """Test case for download_recordings_zip

        Download multiple recordings in zip archive
        """
        pass

    def test_export_static_image_mapper_enrichment(self) -> None:
        """Test case for export_static_image_mapper_enrichment

        Export static image mapper enrichment
        """
        pass

    def test_get_aoi(self) -> None:
        """Test case for get_aoi

        Returns an aoi with {aoi_id}
        """
        pass

    def test_get_aoi_stats(self) -> None:
        """Test case for get_aoi_stats

        List all aois of an enrichment
        """
        pass

    def test_get_aois(self) -> None:
        """Test case for get_aois

        List all aois of an enrichment
        """
        pass

    def test_get_apriltag_detections(self) -> None:
        """Test case for get_apriltag_detections

        Get apritag data for surface enrichment
        """
        pass

    def test_get_apriltags_at_timestamp(self) -> None:
        """Test case for get_apriltags_at_timestamp

        """
        pass

    def test_get_canny_sso_token(self) -> None:
        """Test case for get_canny_sso_token

        Returns the canny
        """
        pass

    def test_get_download_heatmap(self) -> None:
        """Test case for get_download_heatmap

        download zip file with heatmaps
        """
        pass

    def test_get_filter(self) -> None:
        """Test case for get_filter

        Returns a filter with {filter_id}
        """
        pass

    def test_get_filters(self) -> None:
        """Test case for get_filters

        List all filters
        """
        pass

    def test_get_hardware(self) -> None:
        """Test case for get_hardware

        Returns calibration
        """
        pass

    def test_get_heatmap(self) -> None:
        """Test case for get_heatmap

        get heatmap image or json data
        """
        pass

    def test_get_heatmap_background(self) -> None:
        """Test case for get_heatmap_background

        get heatmap background for overlay
        """
        pass

    def test_get_label(self) -> None:
        """Test case for get_label

        Returns a label with {label_id}
        """
        pass

    def test_get_labels(self) -> None:
        """Test case for get_labels

        List all labels
        """
        pass

    def test_get_markerless(self) -> None:
        """Test case for get_markerless

        Get markerless definition
        """
        pass

    def test_get_markerless_camera_poses(self) -> None:
        """Test case for get_markerless_camera_poses

        get markerless camera poses
        """
        pass

    def test_get_markerless_detections_timeline(self) -> None:
        """Test case for get_markerless_detections_timeline

        Recording markerless detections
        """
        pass

    def test_get_markerless_gaze_on_aoi(self) -> None:
        """Test case for get_markerless_gaze_on_aoi

        get gaze on aoi data for markerless enrichment
        """
        pass

    def test_get_markerless_point_cloud(self) -> None:
        """Test case for get_markerless_point_cloud

        """
        pass

    def test_get_profile(self) -> None:
        """Test case for get_profile

        Returns the current logged in user based on auth token
        """
        pass

    def test_get_project_enrichment(self) -> None:
        """Test case for get_project_enrichment

        Get a project enrichment
        """
        pass

    def test_get_project_enrichment_compute_resource(self) -> None:
        """Test case for get_project_enrichment_compute_resource

        """
        pass

    def test_get_project_enrichments(self) -> None:
        """Test case for get_project_enrichments

        List all project enrichments
        """
        pass

    def test_get_project_events_resource(self) -> None:
        """Test case for get_project_events_resource

        Returns a project's events with {project_id}
        """
        pass

    def test_get_project_recording_events_resource(self) -> None:
        """Test case for get_project_recording_events_resource

        Returns a project's recording event with {project_id} and {recording_id}
        """
        pass

    def test_get_project_recordings_resource(self) -> None:
        """Test case for get_project_recordings_resource

        Returns a project's recordings with {project_id}
        """
        pass

    def test_get_project_resource(self) -> None:
        """Test case for get_project_resource

        Returns a project with {project_id}
        """
        pass

    def test_get_project_unique_events(self) -> None:
        """Test case for get_project_unique_events

        Returns all unique events in a project
        """
        pass

    def test_get_projects_resource(self) -> None:
        """Test case for get_projects_resource

        List all projects
        """
        pass

    def test_get_recording(self) -> None:
        """Test case for get_recording

        Returns a recording with {recording_id}
        """
        pass

    def test_get_recording_blinks(self) -> None:
        """Test case for get_recording_blinks

        Recording blinks
        """
        pass

    def test_get_recording_blinks_timeline(self) -> None:
        """Test case for get_recording_blinks_timeline

        Recording blinks timeline
        """
        pass

    def test_get_recording_events(self) -> None:
        """Test case for get_recording_events

        List recording events
        """
        pass

    def test_get_recording_face_detections(self) -> None:
        """Test case for get_recording_face_detections

        Recording face detections
        """
        pass

    def test_get_recording_face_detections_timeline(self) -> None:
        """Test case for get_recording_face_detections_timeline

        Recording face detections
        """
        pass

    def test_get_recording_files(self) -> None:
        """Test case for get_recording_files

        List recording files
        """
        pass

    def test_get_recording_fixations(self) -> None:
        """Test case for get_recording_fixations

        Recording fixations
        """
        pass

    def test_get_recording_fixations_timeline(self) -> None:
        """Test case for get_recording_fixations_timeline

        Recording fixations timeline
        """
        pass

    def test_get_recording_gaze(self) -> None:
        """Test case for get_recording_gaze

        temporary endpoint for player development
        """
        pass

    def test_get_recording_scanpath(self) -> None:
        """Test case for get_recording_scanpath

        Get list of fixation scanpath points per world frame
        """
        pass

    def test_get_recording_scene_camera_intrinsics(self) -> None:
        """Test case for get_recording_scene_camera_intrinsics

        Get Recording's Scene Camera Intrinsics
        """
        pass

    def test_get_recordings(self) -> None:
        """Test case for get_recordings

        List all recordings
        """
        pass

    def test_get_recordings_events_resource(self) -> None:
        """Test case for get_recordings_events_resource

        """
        pass

    def test_get_render(self) -> None:
        """Test case for get_render

        Get a render enrichment
        """
        pass

    def test_get_static_image_mapper_enrichment(self) -> None:
        """Test case for get_static_image_mapper_enrichment

        Get a static image mapper enrichment
        """
        pass

    def test_get_static_image_mapper_enrichments(self) -> None:
        """Test case for get_static_image_mapper_enrichments

        List all static image mapper enrichments of a project
        """
        pass

    def test_get_static_image_mapper_enrichments_recording_fixations(self) -> None:
        """Test case for get_static_image_mapper_enrichments_recording_fixations

        List all the fixations of a recording's static image mapper enrichments
        """
        pass

    def test_get_surface(self) -> None:
        """Test case for get_surface

        Return surface definition
        """
        pass

    def test_get_surface_corners(self) -> None:
        """Test case for get_surface_corners

        get surface locations for surface enrichment
        """
        pass

    def test_get_surface_detections_timeline(self) -> None:
        """Test case for get_surface_detections_timeline

        Recording surface detections
        """
        pass

    def test_get_surface_gaze_on_aoi(self) -> None:
        """Test case for get_surface_gaze_on_aoi

        get gaze on aoi data for markerless enrichment
        """
        pass

    def test_get_template(self) -> None:
        """Test case for get_template

        Returns a template with {template_id}
        """
        pass

    def test_get_templates(self) -> None:
        """Test case for get_templates

        List all templates
        """
        pass

    def test_get_token(self) -> None:
        """Test case for get_token

        Get an access token
        """
        pass

    def test_get_tokens(self) -> None:
        """Test case for get_tokens

        Get all access tokens
        """
        pass

    def test_get_visualization_config(self) -> None:
        """Test case for get_visualization_config

        Get a visualization config
        """
        pass

    def test_get_visualization_configs(self) -> None:
        """Test case for get_visualization_configs

        List project's visualization configs
        """
        pass

    def test_get_wearer(self) -> None:
        """Test case for get_wearer

        Returns a wearer with {wearer_id}
        """
        pass

    def test_get_wearers(self) -> None:
        """Test case for get_wearers

        List all wearers
        """
        pass

    def test_get_workspace(self) -> None:
        """Test case for get_workspace

        Returns the workspace with {workspace_id}
        """
        pass

    def test_get_workspace_invitation(self) -> None:
        """Test case for get_workspace_invitation

        get workspace inviation for token
        """
        pass

    def test_get_workspace_invitation_0(self) -> None:
        """Test case for get_workspace_invitation_0

        Get workspace invitation for token
        """
        pass

    def test_get_workspace_invitations(self) -> None:
        """Test case for get_workspace_invitations

        List all workspace inviations for current user
        """
        pass

    def test_get_workspace_member(self) -> None:
        """Test case for get_workspace_member

        Get workspace member
        """
        pass

    def test_get_workspace_members(self) -> None:
        """Test case for get_workspace_members

        List all members of workspace {workspace_id}
        """
        pass

    def test_get_workspaces(self) -> None:
        """Test case for get_workspaces

        List all workspaces for a user
        """
        pass

    def test_initialize_markerless(self) -> None:
        """Test case for initialize_markerless

        Create markerless definition
        """
        pass

    def test_initialize_rendering(self) -> None:
        """Test case for initialize_rendering

        Create world render definition
        """
        pass

    def test_list_workspace_invitations(self) -> None:
        """Test case for list_workspace_invitations

        List workspace invitations
        """
        pass

    def test_patch_aoi(self) -> None:
        """Test case for patch_aoi

        Update an aoi
        """
        pass

    def test_patch_filter(self) -> None:
        """Test case for patch_filter

        Update a filter
        """
        pass

    def test_patch_label(self) -> None:
        """Test case for patch_label

        Update a label
        """
        pass

    def test_patch_profile(self) -> None:
        """Test case for patch_profile

        Update user profile
        """
        pass

    def test_patch_project_enrichment_resource(self) -> None:
        """Test case for patch_project_enrichment_resource

        Update a project enrichment
        """
        pass

    def test_patch_project_recording_event_resource(self) -> None:
        """Test case for patch_project_recording_event_resource

        Update a project recording event
        """
        pass

    def test_patch_project_resource(self) -> None:
        """Test case for patch_project_resource

        Update a project
        """
        pass

    def test_patch_recording(self) -> None:
        """Test case for patch_recording

        Update a recording
        """
        pass

    def test_patch_recording_event_resource(self) -> None:
        """Test case for patch_recording_event_resource

        Update a recording event
        """
        pass

    def test_patch_render(self) -> None:
        """Test case for patch_render

        Update a render enrichment
        """
        pass

    def test_patch_rotate_surface_orientation(self) -> None:
        """Test case for patch_rotate_surface_orientation

        Change surface rotation
        """
        pass

    def test_patch_static_image_mapper_enrichment(self) -> None:
        """Test case for patch_static_image_mapper_enrichment

        Update a static image mapper enrichment
        """
        pass

    def test_patch_surface(self) -> None:
        """Test case for patch_surface

        Update surface definition
        """
        pass

    def test_patch_template(self) -> None:
        """Test case for patch_template

        Update a template
        """
        pass

    def test_patch_visualization_config(self) -> None:
        """Test case for patch_visualization_config

        Update a visualization config
        """
        pass

    def test_patch_wearer(self) -> None:
        """Test case for patch_wearer

        Update a wearer
        """
        pass

    def test_patch_workspace_member(self) -> None:
        """Test case for patch_workspace_member

        Patch members of workspace {workspace_id}
        """
        pass

    def test_post_accept_invitation_resource(self) -> None:
        """Test case for post_accept_invitation_resource

        Create workspace member based on invite token
        """
        pass

    def test_post_aoi(self) -> None:
        """Test case for post_aoi

        Create a new aoi
        """
        pass

    def test_post_aoi_0(self) -> None:
        """Test case for post_aoi_0

        Create a new aoi
        """
        pass

    def test_post_aoi_1(self) -> None:
        """Test case for post_aoi_1

        Create a new aoi
        """
        pass

    def test_post_distorted_surface_location(self) -> None:
        """Test case for post_distorted_surface_location

        Set distorted surface corner locations
        """
        pass

    def test_post_download_heatmap(self) -> None:
        """Test case for post_download_heatmap

        download zip file with heatmaps
        """
        pass

    def test_post_filters(self) -> None:
        """Test case for post_filters

        Create a new filter
        """
        pass

    def test_post_heatmap(self) -> None:
        """Test case for post_heatmap

        get heatmap image or json data
        """
        pass

    def test_post_label(self) -> None:
        """Test case for post_label

        Create a new label
        """
        pass

    def test_post_label_0(self) -> None:
        """Test case for post_label_0

        Create a new label
        """
        pass

    def test_post_login(self) -> None:
        """Test case for post_login

        Login the user and return a new session cookie
        """
        pass

    def test_post_logout(self) -> None:
        """Test case for post_logout

        Logout the current user
        """
        pass

    def test_post_project_download_resource(self) -> None:
        """Test case for post_project_download_resource

        Download project data
        """
        pass

    def test_post_project_enrichment(self) -> None:
        """Test case for post_project_enrichment

        Create a new project enrichment
        """
        pass

    def test_post_project_enrichment_cancel_resource(self) -> None:
        """Test case for post_project_enrichment_cancel_resource

        """
        pass

    def test_post_project_enrichment_compute_resource(self) -> None:
        """Test case for post_project_enrichment_compute_resource

        """
        pass

    def test_post_project_enrichment_export_resource(self) -> None:
        """Test case for post_project_enrichment_export_resource

        Export an enrichment data
        """
        pass

    def test_post_project_recording_events_resource(self) -> None:
        """Test case for post_project_recording_events_resource

        Create a new project recording event
        """
        pass

    def test_post_projects_resource(self) -> None:
        """Test case for post_projects_resource

        Create a new project
        """
        pass

    def test_post_recording_event(self) -> None:
        """Test case for post_recording_event

        Create a new recording event
        """
        pass

    def test_post_static_image_mapper_enrichment(self) -> None:
        """Test case for post_static_image_mapper_enrichment

        Create a new static image mapper enrichment
        """
        pass

    def test_post_surface(self) -> None:
        """Test case for post_surface

        Create a new surface definition
        """
        pass

    def test_post_template(self) -> None:
        """Test case for post_template

        Create a new template
        """
        pass

    def test_post_token(self) -> None:
        """Test case for post_token

        Creates a new access token
        """
        pass

    def test_post_unregister(self) -> None:
        """Test case for post_unregister

        Unregisters the currently logged in user
        """
        pass

    def test_post_visualization_config(self) -> None:
        """Test case for post_visualization_config

        Create a new visualization config
        """
        pass

    def test_post_wearer(self) -> None:
        """Test case for post_wearer

        Create a new wearer
        """
        pass

    def test_post_workspace(self) -> None:
        """Test case for post_workspace

        Create a new workspace
        """
        pass

    def test_post_workspace_members_resource(self) -> None:
        """Test case for post_workspace_members_resource

        Add workspace member
        """
        pass

    def test_project_enrichments_export(self) -> None:
        """Test case for project_enrichments_export

        Export an enrichment data
        """
        pass

    def test_put_static_image_mapper_enrichments_recording_fixation(self) -> None:
        """Test case for put_static_image_mapper_enrichments_recording_fixation

        Insert or update coordinates of a particular fixation of recording's
        """
        pass

    def test_scan_markerless(self) -> None:
        """Test case for scan_markerless

        Scan markerless
        """
        pass

    def test_update_workspace(self) -> None:
        """Test case for update_workspace

        Update a workspace
        """
        pass


if __name__ == '__main__':
    unittest.main()
