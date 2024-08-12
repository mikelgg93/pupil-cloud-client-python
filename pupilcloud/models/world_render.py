# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pupilcloud.models.gaze_circle import GazeCircle
from typing import Optional, Set
from typing_extensions import Self

class WorldRender(BaseModel):
    """
    WorldRender
    """ # noqa: E501
    audio: Optional[StrictBool] = True
    gaze_circle: Optional[GazeCircle] = None
    id: Optional[StrictStr] = None
    undistort_frames: Optional[StrictBool] = False
    with_gaze: Optional[StrictBool] = True
    with_scanpath: Optional[StrictBool] = False
    with_timestamps: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["audio", "gaze_circle", "id", "undistort_frames", "with_gaze", "with_scanpath", "with_timestamps"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorldRender from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of gaze_circle
        if self.gaze_circle:
            _dict['gaze_circle'] = self.gaze_circle.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorldRender from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "audio": obj.get("audio") if obj.get("audio") is not None else True,
            "gaze_circle": GazeCircle.from_dict(obj["gaze_circle"]) if obj.get("gaze_circle") is not None else None,
            "id": obj.get("id"),
            "undistort_frames": obj.get("undistort_frames") if obj.get("undistort_frames") is not None else False,
            "with_gaze": obj.get("with_gaze") if obj.get("with_gaze") is not None else True,
            "with_scanpath": obj.get("with_scanpath") if obj.get("with_scanpath") is not None else False,
            "with_timestamps": obj.get("with_timestamps") if obj.get("with_timestamps") is not None else False
        })
        return _obj


