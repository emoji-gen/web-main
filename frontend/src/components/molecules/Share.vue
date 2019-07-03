<template>
	<div class="Share">
		<div class="inner">
			<input type="button" class="twitter sharer button" data-sharer="twitter" data-title="絵文字ジェネレーター使って絵文字を生成しました&#9834; {{url}} #絵文字ジェネレーター" title="Twitter でシェアする" v-sharer>
			<input type="button" class="facebook sharer button" data-sharer="facebook" :data-url="url" title="Facebook でシェアする" v-sharer>
		</div>
	</div>
</template>
