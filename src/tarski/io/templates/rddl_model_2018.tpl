domain {domain_name} {{

    requirements {{ {req_list} }};

    types {{ {type_list} }};

    pvariables {{
{pvar_list}
    }};

    cpfs {{
{cpfs_list}
    }};

    reward = {reward_expr};

    action-preconditions {{
{action_precondition_list}
    }};

}}

instance {instance_name} {{

    domain = {domain_name};

    {object_list}

    {non_fluent_expr}

    init-state {{
        {init_state_fluent_expr}
    }};

    horizon = {horizon};
    discount = {discount};
}}