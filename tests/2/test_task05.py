import os

assets = os.path.dirname(os.path.abspath(__file__)) + "/assets"
cwd = os.getcwd()

COMMAND=f"cat {assets}/passwd | ./looneytised.sh"
OUTPUT="""
arenas_p:x:21008:21000:Marvin the Martian arenas:/u/ipsa/arenas_p/cu:/usr/site/bin/shell
berger_p:x:77518:32016:Marvin the Martian bergeron:/u/epitech_2016/berger_p/cu:/usr/site/bin/shell
bertra_s:x:10426:10002:Wile E. Coyote bertrand:/u/supinternet_2016/bertra_s/cu:/usr/site/bin/shell
challe_b:x:49028:32019:Daffy Duck challe:/u/epitech_2019/challe_b/cu:/usr/site/bin/shell
denis_b:x:61106:2011:Porky Pig denis:/u/epita_2011/denis_b/cu:/usr/site/bin/shell
devroe_b:x:62299:2012:Porky Pig devroe:/u/epita_2012/devroe_b/cu:/usr/site/bin/shell
dupuy_d:x:5411:5000:Porky Pig dupuy:/u/admi/dupuy_d/cu:/usr/site/bin/shell
gandon_a:x:22067:62018:Wile E. Coyote gandon:/u/supbiotech_2018/gandon_a/cu:/usr/site/bin/shell
gicque_b:x:22070:62018:Wile E. Coyote gicquel:/u/supbiotech_2018/gicque_b/cu:/usr/site/bin/shell
guilma_p:x:110586:32017:Marvin the Martian guilmard:/u/epitech_2017/guilma_p/cu:/usr/site/bin/shell
leger_i:x:5087:5000:Marvin the Martian leger:/u/admi/leger_i/cu:/usr/site/bin/shell
mart_-:x:50395:32019:Marvin the Martian martin:/u/epitech_2019/mart_-/cu:/usr/site/bin/shell
mart_9_p:x:50389:32019:Marvin the Martian mart_9:/u/epitech_2019/mart_9_p/cu:/usr/site/bin/shell
mart_s:x:5381:5000:Daffy Duck martins:/u/admi/mart_s/cu:/bin/minishell1
moya_b:x:64362:2014:Porky Pig moya:/u/epita_2014/moya_b/cu:/usr/site/bin/shell
papill_a:x:5569:5000:Wile E. Coyote papillon-lignieres:/u/admi/papill_a/cu:/usr/site/bin/shell
parant_b:x:5593:5000:Porky Pig parant:/u/admi/parant_b/cu:/usr/site/bin/shell
pojer_a:x:5399:5000:Daffy Duck pojer:/u/admi/pojer_a/cu:/usr/site/bin/shell
poney:x:41255:40000:Porky Pig drain:/u/tmp/poney/cu:/usr/site/bin/shell
prost_p:x:75109:32015:Marvin the Martian prost:/u/epitech_2015/prost_p/cu:/usr/site/bin/shell
richar_7:x:50138:32019:Wile E. Coyote richard:/u/epitech_2019/richar_7/cu:/usr/site/bin/shell
sbriss_a:x:5444:5000:Wile E. Coyote sbrissa:/u/admi/sbriss_a/cu:/bin/42sh
sourio_b:x:5261:5000:Porky Pig sourioux:/u/admi/sourio_b/cu:/bin/close
tessa_b:x:73058:32013:Porky Pig tessa:/u/epitech_2013/tessa_b/cu:/usr/site/bin/shell
touati_a:x:10340:10001:Wile E. Coyote touati:/u/supinternet_2015/touati_a/cu:/usr/site/bin/shell
vincen_p:x:64341:2014:Marvin the Martian vincent:/u/epita_2014/vincen_p/cu:/usr/site/bin/shell
weiss_b:x:40864:40000:Porky Pig weiss:/u/tmp/weiss_b/cu:/usr/site/bin/shell
wolff_b:x:73558:32013:Porky Pig wolff:/u/epitech_2013/wolff_b/cu:/usr/site/bin/shell
"""
