# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/artifact/events/infrastructure/dbus/dbus_artifact_tag_pushed.py

This file defines the DbusArtifactTagPushed class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/artifact-event-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import signal
import json
from pythoneda.shared import Event, Invariants
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.artifact.artifact.events import ArtifactTagPushed
from pythoneda.shared.artifact.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List, Type


class DbusArtifactTagPushed(DbusEvent):
    """
    D-Bus interface for TagPushed

    Class name: DbusArtifactTagPushed

    Responsibilities:
        - Define the d-bus interface for the ArtifactTagPushed event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusArtifactTagPushed.
        """
        super().__init__(DBUS_PATH)

    @classmethod
    @property
    def name(cls) -> str:
        """
        Retrieves the d-bus interface name.
        :return: Such value.
        :rtype: str
        """
        return "Pythoneda_Shared_Artifact_Artifact_Events_ArtifactTagPushed"

    @signal()
    def TagPushed(self, tag: "s", commit: "s", repositoryUrl: "s", branch: "s"):
        """
        Defines the ArtifactTagPushed d-bus signal.
        :param tag: The tag.
        :type tag: str
        :param commit: The commit.
        :type commit: str
        :param repositoryUrl: The repository url.
        :type repositoryUrl: str
        :param branch: The branch.
        :type branch: str
        """
        pass

    @classmethod
    def transform(cls, event: TagPushed) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.artifact.events.ArtifactTagPushed
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.tag,
            event.commit,
            event.repository_url,
            event.branch,
            json.dumps(event.previous_event_ids),
            Invariants.instance().to_json(event),
            event.id,
        ]

    @classmethod
    def sign(cls, event: ArtifactTagPushed) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.artifact.events.ArtifactTagPushed
        :return: The signature.
        :rtype: str
        """
        return "sssssss"

    @classmethod
    def parse(cls, message: Message) -> ArtifactTagPushed:
        """
        Parses given d-bus message containing a ArtifactTagPushed event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The TagPushed event.
        :rtype: pythoneda.shared.artifact.artifact.events.ArtifactTagPushed
        """
        tag, commit, repository_url, branch, prev_event_ids, invariants, event_id = (
            message.body
        )
        return (
            invariants,
            ArtifactTagPushed(
                tag,
                commit,
                repository_url,
                branch,
                json.loads(prev_event_ids),
                event_id,
            ),
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return ArtifactTagPushed


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
