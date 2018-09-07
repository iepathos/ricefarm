#!/bin/bash

if [ -z "${1}" ]; then
	loop=10
else
	loop=${1}
fi

watch --color -n "${loop}" ./rotate_backgrounds.py ~/backgrounds
