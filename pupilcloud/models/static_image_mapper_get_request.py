# coding: utf-8

"""
Pupil Cloud

Pupil Cloud API

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self


class StaticImageMapperGetRequest(BaseModel):
    """
    StaticImageMapperGetRequest
    """  # noqa: E501

    created_at: Optional[datetime] = None
    created_by_user_id: Optional[StrictStr] = None
    deleted_by_user_id: Optional[StrictStr] = None
    error_message: Optional[StrictStr] = Field(
        default=None, description="static enrichment error message"
    )
    fixations_status: Optional[List[Any]] = None
    from_event_name: StrictStr
    id: Optional[StrictStr] = None
    kind: Optional[StrictStr] = Field(default=None, description="the enrichment kind")
    name: StrictStr
    project_id: Optional[StrictStr] = None
    slices: Optional[List[Any]] = None
    static_image_id: Optional[StrictStr] = None
    static_image_image_thumbnail_url: Optional[StrictStr] = None
    status: Optional[Any] = None
    to_event_name: StrictStr
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = [
        "created_at",
        "created_by_user_id",
        "deleted_by_user_id",
        "error_message",
        "fixations_status",
        "from_event_name",
        "id",
        "kind",
        "name",
        "project_id",
        "slices",
        "static_image_id",
        "static_image_image_thumbnail_url",
        "status",
        "to_event_name",
        "updated_at",
    ]

    @field_validator("kind")
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "marker-mapper",
                "slam-mapper",
                "render",
                "raw-data-export",
                "face-mapper",
                "static-image-mapper",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('marker-mapper', 'slam-mapper', 'render', 'raw-data-export', 'face-mapper', 'static-image-mapper')"
            )
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
        """Create an instance of StaticImageMapperGetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in fixations_status (list)
        _items = []
        if self.fixations_status:
            for _item in self.fixations_status:
                if _item:
                    _items.append(_item.to_dict())
            _dict["fixations_status"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in slices (list)
        _items = []
        if self.slices:
            for _item in self.slices:
                if _item:
                    _items.append(_item.to_dict())
            _dict["slices"] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StaticImageMapperGetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created_at": obj.get("created_at"),
                "created_by_user_id": obj.get("created_by_user_id"),
                "deleted_by_user_id": obj.get("deleted_by_user_id"),
                "error_message": obj.get("error_message"),
                "fixations_status": obj.get("fixations_status"),
                "from_event_name": obj.get("from_event_name"),
                "id": obj.get("id"),
                "kind": obj.get("kind"),
                "name": obj.get("name"),
                "project_id": obj.get("project_id"),
                "slices": obj["slices"],
                "static_image_id": obj.get("static_image_id"),
                "static_image_image_thumbnail_url": obj.get(
                    "static_image_image_thumbnail_url"
                ),
                "status": obj.get("status"),
                "to_event_name": obj.get("to_event_name"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
