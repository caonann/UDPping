#!/bin/bash
taskset 0x00000001 socat -v UDP-LISTEN:4000,fork PIPE