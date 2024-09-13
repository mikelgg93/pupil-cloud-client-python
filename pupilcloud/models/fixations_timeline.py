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

class FixationsTimeline(BaseModel):
    """
    FixationsTimeline
    """ # noqa: E501
    end_timestamp: Optional[Union[StrictFloat, StrictInt]] = None
    has_fixations: Optional[StrictInt] = None
    max_fixation_id: Optional[StrictInt] = None
    min_fixation_id: Optional[StrictInt] = None
    start_timestamp: Optional[Union[StrictFloat, StrictInt]] = None
    total_fixations_count: Optional[StrictInt] = None
    total_frames: Optional[StrictInt] = None
    unique_fixations_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["end_timestamp", "has_fixations", "max_fixation_id", "min_fixation_id", "start_timestamp", "total_fixations_count", "total_frames", "unique_fixations_count"]

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
        """Create an instance of FixationsTimeline from a JSON string"""
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
        """Create an instance of FixationsTimeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "end_timestamp": obj.get("end_timestamp"),
            "has_fixations": obj.get("has_fixations"),
            "max_fixation_id": obj.get("max_fixation_id"),
            "min_fixation_id": obj.get("min_fixation_id"),
            "start_timestamp": obj.get("start_timestamp"),
            "total_fixations_count": obj.get("total_fixations_count"),
            "total_frames": obj.get("total_frames"),
            "unique_fixations_count": obj.get("unique_fixations_count")
        })
        return _obj


