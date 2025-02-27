from click._compat import should_strip_ansi


def test_is_jupyter_kernel_output():
    class JupyterKernelFakeStream:
        pass

    # implementation detail, aka cheapskate test
    JupyterKernelFakeStream.__module__ = "ipykernel.faked"
    assert not should_strip_ansi(stream=JupyterKernelFakeStream())

def test_color_policy_auto():
    # assume default ColorPolicy is set to AUTO, check that when we print something with color to TTY, it is colored
    # but when it is e.g. piped to a file, it is not colored
    # use secho to print colored text

    class JupyterKernelFakeStream:
        pass

    # implementation detail, aka cheapskate test
    JupyterKernelFakeStream.__module__ = "ipykernel.faked"
    assert should_strip_ansi(stream=JupyterKernelFakeStream()) == False
    
    # test for non-TTY
    class NonTTYStream:
        pass
    
    assert should_strip_ansi(stream=NonTTYStream()) == True

    
def test_color_policy_always_keep():
    
    from click import set_color_policy, ColorPolicy
    class JupyterKernelFakeStream:
        pass
    
    
    set_color_policy(ColorPolicy.ALWAYS_KEEP)

    JupyterKernelFakeStream.__module__ = "ipykernel.faked"
    assert should_strip_ansi(stream=JupyterKernelFakeStream()) == False

    set_color_policy(ColorPolicy.AUTO)


def test_color_policy_always_strip():
    
    from click import set_color_policy, ColorPolicy
    class JupyterKernelFakeStream:
        pass
    
    
    set_color_policy(ColorPolicy.ALWAYS_STRIP)

    JupyterKernelFakeStream.__module__ = "ipykernel.faked"
    assert should_strip_ansi(stream=JupyterKernelFakeStream()) == True

    set_color_policy(ColorPolicy.AUTO)
