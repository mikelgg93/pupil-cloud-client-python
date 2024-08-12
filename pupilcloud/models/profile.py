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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Profile(BaseModel):
    """
    Profile
    """ # noqa: E501
    default_workspace_id: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    email_verified: Optional[StrictBool] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    onboarded_at: Optional[datetime] = None
    photo_url: Optional[StrictStr] = None
    product_updates_subscribed: Optional[StrictBool] = None
    provider: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    user_workspaces: Optional[List[WorkspaceMembership]] = None
    __properties: ClassVar[List[str]] = ["default_workspace_id", "email", "email_verified", "id", "name", "onboarded_at", "photo_url", "product_updates_subscribed", "provider", "uid", "user_workspaces"]

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
        """Create an instance of Profile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "email",
            "email_verified",
            "id",
            "provider",
            "uid",
            "user_workspaces",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in user_workspaces (list)
        _items = []
        if self.user_workspaces:
            for _item in self.user_workspaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['user_workspaces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Profile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default_workspace_id": obj.get("default_workspace_id"),
            "email": obj.get("email"),
            "email_verified": obj.get("email_verified"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "onboarded_at": obj.get("onboarded_at"),
            "photo_url": obj.get("photo_url"),
            "product_updates_subscribed": obj.get("product_updates_subscribed"),
            "provider": obj.get("provider"),
            "uid": obj.get("uid"),
            "user_workspaces": [WorkspaceMembership.from_dict(_item) for _item in obj["user_workspaces"]] if obj.get("user_workspaces") is not None else None
        })
        return _obj


