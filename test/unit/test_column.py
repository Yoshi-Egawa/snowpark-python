#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2021 Snowflake Computing Inc. All right reserved.
#
from src.snowflake.snowpark.functions import col
from src.snowflake.snowpark.internal.sp_expressions import LeafExpression as SPLeafExpression


def test_getName():
    """Test getName() of Column."""
    name = col("id").getName()
    assert name == '"ID"'

    # LeafExpression is not named Expression, so should not return a name
    name = col(SPLeafExpression()).getName()
    assert not name