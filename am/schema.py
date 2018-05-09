#!/usr/bin/env python
# -*- coding: utf-8 -*-
import graphene

import finance.schema
import general.schema
import legislative.schema

class Query(finance.schema.Query, general.schema.Query, legislative.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)