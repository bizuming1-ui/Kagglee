# Q44：如何处理Notebook中bootstrap成功sys.exit(0)？

A 忽略所有异常：不选，会掩盖失败。B 仅捕获SystemExit并按Python语义返回成功/失败码：推荐并选择。C 重新启动所有服务：不选，当前已ready。D 将所有退出码改0：不选，误报成功。

用户提供双T4真实启动ready日志，195秒；不因此签收推理/训练/音质。此次仅修调用返回，不重启远程服务。未开Q45。

## 下一题之前50条复核行动

1. 对成功SystemExit(0)，只规范化SystemExit而非捕获所有BaseException。
2. 对成功SystemExit(0)，校验成功返回0且后续语句可继续执行。
3. 对成功SystemExit(0)，校验非零失败不被转成0。
4. 对成功SystemExit(0)，校验字符串失败不回显私有异常原文。
5. 对成功SystemExit(0)，不发kill或重复启动已就绪服务。
6. 对成功SystemExit(0)，保持上版Colab/Jupyter参数隔离和严格CLI。
7. 对成功SystemExit(0)，核对58个运行资产和旧包字节不变。
8. 对成功SystemExit(0)，以真实IPython及CPU替身区分验证范围。
9. 对成功SystemExit(0)，只读GET现有health且不读取token。
10. 对成功SystemExit(0)，把启动ready与模型推理/训练/音质/速度签收分开。
11. 对成功SystemExit(None)，只规范化SystemExit而非捕获所有BaseException。
12. 对成功SystemExit(None)，校验成功返回0且后续语句可继续执行。
13. 对成功SystemExit(None)，校验非零失败不被转成0。
14. 对成功SystemExit(None)，校验字符串失败不回显私有异常原文。
15. 对成功SystemExit(None)，不发kill或重复启动已就绪服务。
16. 对成功SystemExit(None)，保持上版Colab/Jupyter参数隔离和严格CLI。
17. 对成功SystemExit(None)，核对58个运行资产和旧包字节不变。
18. 对成功SystemExit(None)，以真实IPython及CPU替身区分验证范围。
19. 对成功SystemExit(None)，只读GET现有health且不读取token。
20. 对成功SystemExit(None)，把启动ready与模型推理/训练/音质/速度签收分开。
21. 对正常函数返回，只规范化SystemExit而非捕获所有BaseException。
22. 对正常函数返回，校验成功返回0且后续语句可继续执行。
23. 对正常函数返回，校验非零失败不被转成0。
24. 对正常函数返回，校验字符串失败不回显私有异常原文。
25. 对正常函数返回，不发kill或重复启动已就绪服务。
26. 对正常函数返回，保持上版Colab/Jupyter参数隔离和严格CLI。
27. 对正常函数返回，核对58个运行资产和旧包字节不变。
28. 对正常函数返回，以真实IPython及CPU替身区分验证范围。
29. 对正常函数返回，只读GET现有health且不读取token。
30. 对正常函数返回，把启动ready与模型推理/训练/音质/速度签收分开。
31. 对失败SystemExit(1/2/3/130)，只规范化SystemExit而非捕获所有BaseException。
32. 对失败SystemExit(1/2/3/130)，校验成功返回0且后续语句可继续执行。
33. 对失败SystemExit(1/2/3/130)，校验非零失败不被转成0。
34. 对失败SystemExit(1/2/3/130)，校验字符串失败不回显私有异常原文。
35. 对失败SystemExit(1/2/3/130)，不发kill或重复启动已就绪服务。
36. 对失败SystemExit(1/2/3/130)，保持上版Colab/Jupyter参数隔离和严格CLI。
37. 对失败SystemExit(1/2/3/130)，核对58个运行资产和旧包字节不变。
38. 对失败SystemExit(1/2/3/130)，以真实IPython及CPU替身区分验证范围。
39. 对失败SystemExit(1/2/3/130)，只读GET现有health且不读取token。
40. 对失败SystemExit(1/2/3/130)，把启动ready与模型推理/训练/音质/速度签收分开。
41. 对负整数失败退出码，只规范化SystemExit而非捕获所有BaseException。
42. 对负整数失败退出码，校验成功返回0且后续语句可继续执行。
43. 对负整数失败退出码，校验非零失败不被转成0。
44. 对负整数失败退出码，校验字符串失败不回显私有异常原文。
45. 对负整数失败退出码，不发kill或重复启动已就绪服务。
46. 对负整数失败退出码，保持上版Colab/Jupyter参数隔离和严格CLI。
47. 对负整数失败退出码，核对58个运行资产和旧包字节不变。
48. 对负整数失败退出码，以真实IPython及CPU替身区分验证范围。
49. 对负整数失败退出码，只读GET现有health且不读取token。
50. 对负整数失败退出码，把启动ready与模型推理/训练/音质/速度签收分开。
