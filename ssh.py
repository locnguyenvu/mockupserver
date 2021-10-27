import os
import subprocess

result = subprocess.run(['ssh', '-i', '~/.ssh/zalora_id_rsa', '-J', 'zjumper', 'loc.nguyenvu@54.255.187.156', 'ENV=live', './cpx', '-c', 'id', 'catalog-api/products/products-info-by-config-skus', 'configSkus=A82DCAABF71BF0GS'], stdout=subprocess.PIPE)
print(result.stdout)