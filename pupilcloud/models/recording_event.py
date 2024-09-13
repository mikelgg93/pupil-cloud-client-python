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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Set
from typing_extensions import Self

class RecordingEvent(BaseModel):
    """
    RecordingEvent
    """ # noqa: E501
    created_at: Optional[datetime] = None
    created_by_user_id: Optional[StrictStr] = None
    epoch_ns: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    offset_s: Optional[Union[StrictFloat, StrictInt]] = None
    origin: StrictStr = Field(description="origin of the event")
    recording_id: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["created_at", "created_by_user_id", "epoch_ns", "id", "name", "offset_s", "origin", "recording_id", "updated_at"]

    @field_validator('origin')
    def origin_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['recording', 'cloud']):
            raise ValueError("must be one of enum values ('recording', 'cloud')")
        return value

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
        """Create an instance of RecordingEvent from a JSON string"""
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
        """Create an instance of RecordingEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "created_by_user_id": obj.get("created_by_user_id"),
            "epoch_ns": obj.get("epoch_ns"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "offset_s": obj.get("offset_s"),
            "origin": obj.get("origin"),
            "recording_id": obj.get("recording_id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


