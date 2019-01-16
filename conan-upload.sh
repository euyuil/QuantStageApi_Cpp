#!/bin/bash

conan remove QuantStageApi/20190107@liuyuesoft/stable --packages -f
conan create . QuantStageApi/20190107@liuyuesoft/stable -s compiler.version=5.4
conan create . QuantStageApi/20190107@liuyuesoft/stable -s compiler.version=4.8
# conan export-pkg . QuantStageApi/20190107@liuyuesoft/stable -s compiler.version=5.4 -f
# conan export-pkg . QuantStageApi/20190107@liuyuesoft/stable -s compiler.version=4.8 -f
conan upload QuantStageApi/20190107@liuyuesoft/stable --all -r=liuyuesoft
