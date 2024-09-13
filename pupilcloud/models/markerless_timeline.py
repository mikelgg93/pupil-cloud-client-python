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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Set
from typing_extensions import Self

class MarkerlessTimeline(BaseModel):
    """
    MarkerlessTimeline
    """ # noqa: E501
    aoi_detected: Optional[Union[StrictFloat, StrictInt]] = None
    avg_gaze_on_aoi: Optional[Union[StrictFloat, StrictInt]] = None
    end_timestamp: Optional[Union[StrictFloat, StrictInt]] = None
    gaze_on_aoi: Optional[Union[StrictFloat, StrictInt]] = None
    start_timestamp: Optional[Union[StrictFloat, StrictInt]] = None
    sum_gaze_on_aoi: Optional[StrictInt] = None
    total_frames: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["aoi_detected", "avg_gaze_on_aoi", "end_timestamp", "gaze_on_aoi", "start_timestamp", "sum_gaze_on_aoi", "total_frames"]

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
        """Create an instance of MarkerlessTimeline from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MarkerlessTimeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aoi_detected": obj.get("aoi_detected"),
            "avg_gaze_on_aoi": obj.get("avg_gaze_on_aoi"),
            "end_timestamp": obj.get("end_timestamp"),
            "gaze_on_aoi": obj.get("gaze_on_aoi"),
            "start_timestamp": obj.get("start_timestamp"),
            "sum_gaze_on_aoi": obj.get("sum_gaze_on_aoi"),
            "total_frames": obj.get("total_frames")
        })
        return _obj


