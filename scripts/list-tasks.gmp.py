# -*- coding: utf-8 -*-
# Copyright (C) 2019-2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gvmtools.helper import Table
from argparse import Namespace
from gvm.protocols.gmp import Gmp


def main(gmp: Gmp, args: Namespace) -> None:
    # pylint: disable=unused-argument

    response_xml = gmp.get_tasks()
    tasks_xml = response_xml.xpath('task')

    heading = ['ID', 'Name', 'Severity']

    rows = []

    for task in tasks_xml:
        name = ''.join(task.xpath('name/text()'))
        task_id = task.get('id')
        severity = ''.join(task.xpath('last_report/report/severity/text()'))

        rows.append([task_id, name, severity])

    print(Table(heading=heading, rows=rows))


if __name__ == '__gmp__':
    main(gmp, args)
