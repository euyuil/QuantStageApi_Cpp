#!/bin/bash

conan remove QuantStageApi/20190107@liuyuesoft/stable --packages -f
conan export-pkg . QuantStageApi/20190107@liuyuesoft/stable -s compiler.version=5
conan export-pkg . QuantStageApi/20190107@liuyuesoft/stable -s compiler.version=4.8
conan upload QuantStageApi/20190107@liuyuesoft/stable --all -r=liuyuesoft
