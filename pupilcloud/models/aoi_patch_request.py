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
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class AoiPatchRequest(BaseModel):
    """
    AoiPatchRequest
    """ # noqa: E501
    bounding_box: Optional[StrictStr] = None
    centroid_xy: Optional[StrictStr] = None
    color: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    enrichment_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    mask_image_data_url: Optional[StrictStr] = None
    name: StrictStr
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["bounding_box", "centroid_xy", "color", "description", "enrichment_id", "id", "mask_image_data_url", "name", "updated_at"]

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
        """Create an instance of AoiPatchRequest from a JSON string"""
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
        """Create an instance of AoiPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bounding_box": obj.get("bounding_box"),
            "centroid_xy": obj.get("centroid_xy"),
            "color": obj.get("color"),
            "description": obj.get("description"),
            "enrichment_id": obj.get("enrichment_id"),
            "id": obj.get("id"),
            "mask_image_data_url": obj.get("mask_image_data_url"),
            "name": obj.get("name"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


