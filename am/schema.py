#!/usr/bin/env python
# -*- coding: utf-8 -*-
import graphene

import finance.schema

class Query(finance.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)